# Call_test.py

import os
import tempfile
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(headless=False):
    options = Options()
    options.add_argument("--start-maximized")

    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    # ✅ Only use temp profile locally (never in CI/CD)
    if os.getenv("GITHUB_ACTIONS"):
        options.add_argument("--guest")
        options.add_argument("--incognito")
    else:
        temp_profile = tempfile.mkdtemp()
        options.add_argument(f"--user-data-dir={temp_profile}")

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
    # 🔹 Run headless in CI/CD, GUI locally
    headless = bool(os.getenv("GITHUB_ACTIONS"))
    test_openhome_login(headless=headless)
