# Simple Selenium Login Script (works locally & in CI/CD)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import tempfile
import time

# Chrome options
options = Options()
options.add_argument("--start-maximized")

# Extra flags for GitHub Actions / CI
options.add_argument("--headless")          # Run in headless mode (no UI in CI)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Unique user-data-dir (avoids "already in use" errors in CI)
options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)

# Open the URL
driver.get("https://app.openhome.xyz")

# Login
driver.find_element(By.NAME, "email").send_keys("mohsinalilkl@gmail.com")
driver.find_element(By.NAME, "password").send_keys("12345678")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait a bit so you can confirm login worked
time.sleep(5)

# Exit logic
if __name__ == "__main__":
    try:
        input("✅ Logged in successfully. Press Enter to close...")  # Local run
    except EOFError:
        time.sleep(5)  # CI fallback
    driver.quit()
