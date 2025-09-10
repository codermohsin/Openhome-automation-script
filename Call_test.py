# Call_test.py

import os
import sys
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

    # ✅ Only add headless/CI flags if requested
    if headless:
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    # Always create fresh user profile
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    return driver


def test_openhome_login():
    # Detect environment → default: GUI for local, Headless for CI
    headless = os.getenv("CI", "false").lower() == "true"

    driver = get_driver(headless=headless)

    try:
        # Open the URL
        driver.get("https://app.openhome.xyz")

        # Login
        driver.find_element(By.NAME, "email").send_keys("mohsinalilkl@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("12345678")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Verify successful login
        time.sleep(5)
        assert "dashboard" in driver.current_url.lower() or "openhome" in driver.page_source.lower()

    finally:
        if not headless:
            input("Press Enter to close browser...")  # keep browser open locally
        driver.quit()


if __name__ == "__main__":
    # Allow overriding via command line: python Call_test.py --headless
    headless_flag = "--headless" in sys.argv
    os.environ["CI"] = "true" if headless_flag else "false"
    test_openhome_login()
