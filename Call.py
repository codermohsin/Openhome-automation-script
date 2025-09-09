from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # Added for auto WebDriver management
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

# Automatically download and use the correct Chrome WebDriver
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)  # wait up to 10 seconds for elements to be found

# Open the URL
driver.get("https://app.openhome.xyz")

# Interact with the login form
driver.find_element(By.NAME, "email").send_keys("mohsinalilkl@gmail.com")
driver.find_element(By.NAME, "password").send_keys("12345678")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//li[@id='Openhome']").click()
time.sleep(20)
driver.find_element(By.XPATH,"//input[@id='myInput']").send_keys("Hello can you tell me about yourself in details?")
driver.find_element(By.XPATH,"//button[@id='myBtn']").click()
time.sleep(20)
driver.find_element(By.XPATH,"//button[@id='start_conversation']").click()

# Keep browser open until user presses Enter
input("Press Enter to close the browser...")
driver.quit()

# Keep browser open for 10 seconds
# time.sleep(10)

# Close the browser
# driver.quit()
