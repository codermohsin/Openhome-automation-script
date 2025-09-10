# Call_test.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import tempfile
import time
import sys
import os

try:
    import pytest  # ✅ Only used in GitHub Actions
except ImportError:
    pytest = None


def get_driver(headless=False):
    options = Options()
    options.add_argument("--start-maximized")

    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    # 🚨 FIX: skip user-data-dir on GitHub Actions (causing "session not created")
    if not os.getenv("GITHUB_ACTIONS"):
        options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    return driver


def test_openhome_login(headless=False):
    driver = get_driver(headless=headless)
    try:
        driver.get("https://app.openhome.xyz")

        driver.find_element(By.NAME, "email").send_keys("mohsinalilkl@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("12345678")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(5)
        assert "dashboard" in driver.current_url.lower() or "openhome" in driver.page_source.lower()

    finally:
        driver.quit()


if __name__ == "__main__":
    # ✅ Detect mode
    headless = "--headless" in sys.argv or bool(os.getenv("GITHUB_ACTIONS"))
    test_openhome_login(headless=headless)
