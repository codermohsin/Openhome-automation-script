# Call_test.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import tempfile
import time

def test_openhome_login():
    # Chrome options
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")          # CI headless run
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

    # Initialize WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    try:
        # Open the URL
        driver.get("https://app.openhome.xyz")

        # Login
        driver.find_element(By.NAME, "email").send_keys("mohsinalilkl@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("12345678")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # ✅ Small check: page title or some element after login
        time.sleep(5)
        assert "dashboard" in driver.current_url.lower() or "openhome" in driver.page_source.lower()

    finally:
        driver.quit()
