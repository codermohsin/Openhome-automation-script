# CI/CD Pipeline for Selenium Script
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import tempfile

# Set Chrome options
options = Options()
options.add_argument("--start-maximized")

# Extra flags for GitHub Actions / CI
options.add_argument("--headless")          # Run in headless mode (no UI)
options.add_argument("--no-sandbox")        # Required in CI
options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory crashes

# Give each run a unique user-data-dir to avoid "already in use" errors
options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

# Auto-allow camera and mic permissions
prefs = {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
}
options.add_experimental_option("prefs", prefs)

# Automatically download and use the correct Chrome WebDriver
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)

# Open the URL
driver.get("https://app.openhome.xyz")

# Interact with the login form
driver.find_element(By.NAME, "email").send_keys("mohsinalilkl@gmail.com")
driver.find_element(By.NAME, "password").send_keys("12345678")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# ✅ Explicit wait for "Openhome" to be clickable
wait = WebDriverWait(driver, 20)
openhome_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//li[@id='Openhome']"))
)
openhome_button.click()

# Wait before sending a message
time.sleep(10)

driver.find_element(By.XPATH, "//input[@id='myInput']").send_keys(
    "Hello can you tell me about yourself in details?"
)
driver.find_element(By.XPATH, "//button[@id='myBtn']").click()

time.sleep(10)

driver.find_element(By.XPATH, "//button[@id='start_conversation']").click()

# ✅ In CI we can’t wait for user input, so just wait a bit then quit
if __name__ == "__main__":
    try:
        input("Press Enter to close the browser...")
    except EOFError:
        # In CI → fallback to timed quit
        time.sleep(10)
    driver.quit()
