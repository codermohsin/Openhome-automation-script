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

# --- Setup Chrome Options ---
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--headless")                  # Run headless in CI
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

# Auto-allow camera/mic/notifications
prefs = {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
}
options.add_experimental_option("prefs", prefs)

# --- Initialize Driver ---
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 20)

# --- Safe open with retries ---
def safe_open(driver, url, retries=3):
    for i in range(retries):
        try:
            driver.get(url)
            return
        except Exception as e:
            print(f"⚠️ Attempt {i+1} to open {url} failed: {e}")
            time.sleep(5)
    raise RuntimeError(f"❌ Could not open {url} after {retries} attempts")

# --- Test Steps ---
safe_open(driver, "https://app.openhome.xyz")

# Login with requested credentials
driver.find_element(By.NAME, "email").send_keys("mohsinalilkl@gmail.com")
driver.find_element(By.NAME, "password").send_keys("12345678")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait for dashboard / Openhome tab
openhome_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//li[@id='Openhome']"))
)
openhome_button.click()

# Interact with input + send message
msg_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='myInput']")))
msg_box.send_keys("Hello, can you tell me about yourself in detail?")
driver.find_element(By.XPATH, "//button[@id='myBtn']").click()

time.sleep(5)

# Start conversation
start_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='start_conversation']"))
)
start_btn.click()

# --- Quit logic ---
if __name__ == "__main__":
    try:
        input("Press Enter to close the browser...")  # For local runs
    except EOFError:
        time.sleep(10)  # For CI/CD
    driver.quit()
