from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set Chrome options 
options = Options()
options.add_argument("--start-maximized")  # Open browser in maximized mode

# Auto-allow camera and mic permissions
prefs = {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
}
options.add_experimental_option("prefs", prefs)

# Initialize WebDriver with webdriver-manager (auto handles correct ChromeDriver)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 20)

# Open the URL
driver.get("https://app.openhome.xyz")

# Interact with the login form
driver.find_element(By.NAME, "email").send_keys("mohsinalilkl@gmail.com")
driver.find_element(By.NAME, "password").send_keys("12345678")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait for and click on the specific marketplace button
market_xpath = "//div[@class='market-place-features-body']//div[3]//div[2]//div[2]//button[2]//div[1]"
try:
    marketplace_button = wait.until(EC.presence_of_element_located((By.XPATH, market_xpath)))
    driver.execute_script("arguments[0].scrollIntoView({block:'center', inline:'center'});", marketplace_button)
    time.sleep(0.5)
    try:
        marketplace_button.click()
    except ElementClickInterceptedException:
        try:
            clickable = wait.until(EC.element_to_be_clickable((By.XPATH, market_xpath)))
            clickable.click()
        except Exception:
            driver.execute_script("arguments[0].click();", marketplace_button)
except TimeoutException:
    print("Marketplace button not found.")

# Send first message
time.sleep(10)
driver.find_element(By.XPATH, "//input[@id='myInput']").send_keys("Hello can you tell me about yourself")
driver.find_element(By.XPATH, "//button[@id='myBtn']").click()

# Select from react-select-2
time.sleep(10)
driver.find_element(By.ID, "react-select-2-input").click()
driver.find_elements(By.XPATH, "//div[@role='option']")[1].click()

# Send second message
time.sleep(10)
driver.find_element(By.XPATH, "//input[@id='myInput']").send_keys("Tell me about Openhome")
driver.find_element(By.XPATH, "//button[@id='myBtn']").click()

# Select from react-select-3
time.sleep(10)
driver.find_element(By.ID, "react-select-3-input").click()
driver.find_elements(By.XPATH, "//div[@role='option']")[2].click()

# Send third message
time.sleep(10)
driver.find_element(By.XPATH, "//input[@id='myInput']").send_keys("Tell me about Openhome")
driver.find_element(By.XPATH, "//button[@id='myBtn']").click()

# Keep browser open until user presses Enter
input("Press Enter to close the browser...")
driver.quit()
