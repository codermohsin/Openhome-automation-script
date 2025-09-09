from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
driver.find_element(By.CSS_SELECTOR,"nav[class='navbar-container'] button[class='create-nav-btn flexCenter']").click()
driver.find_element(By.CSS_SELECTOR,"div[class='ReactModalPortal'] button:nth-child(1) img:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR,"div[class='ReactModalPortal'] button:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Name']").send_keys("Testing_Personality")
driver.find_element(By.CSS_SELECTOR,"textarea[placeholder='Description']").send_keys("This is the description for the testing personality")
driver.find_element(By.CSS_SELECTOR,"div[class='chakra-stack quick-create-label-div css-1yt3bq9'] div:nth-child(2)").click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.find_element(By.XPATH,"//button[normalize-space()='Save Personality']").click()

# Keep browser open until user presses Enter
input("Press Enter to close the browser...")
driver.quit()

# Keep browser open for 10 seconds
# time.sleep(10)

# Close the browser.
# driver.quit()
