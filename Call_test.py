# Call_test.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


def get_driver(headless=False, ci_mode=False):
    options = Options()
    options.add_argument("--start-maximized")

    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    if not ci_mode:  
        # ✅ Local run only (GUI mode, user profile)
        options.add_argument("--incognito")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    return driver


def test_openhome_login():
    # Detect if running in GitHub Actions
    ci_mode = os.getenv("GITHUB_ACTIONS") == "true"

    driver = get_driver(headless=ci_mode, ci_mode=ci_mode)
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
    test_openhome_login()
