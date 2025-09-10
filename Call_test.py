import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def driver():
    options = ChromeOptions()
    options.add_argument("--headless=new")  # ✅ for CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_openhome_login(driver):
    driver.get("https://sporepress.org/login")
    wait = WebDriverWait(driver, 40)

    # ✅ Login step
    email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[contains(., 'Login')]")

    email_field.send_keys("QA_Engineer@gmail.com")
    password_field.send_keys("12345678")
    login_button.click()

    # ✅ Wait until redirected to dashboard
    wait.until(EC.url_contains("/dashboard/home"))

    # ✅ Try to find Openhome button
    try:
        openhome_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//li[@id='Openhome']"))
        )
    except Exception:
        print("⚠️ Element with id='Openhome' not clickable, trying by text...")
        try:
            openhome_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//li[contains(., 'Openhome')]"))
            )
        except Exception:
            # Print page source for debugging in CI
            print("❌ Could not locate 'Openhome' element. Dumping page source:")
            print(driver.page_source)
            raise

    openhome_button.click()
    time.sleep(3)

    # ✅ Assert that Openhome page is visible
    assert "Openhome" in driver.page_source
