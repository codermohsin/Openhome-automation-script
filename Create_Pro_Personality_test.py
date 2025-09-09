from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
driver.implicitly_wait(10)

# Open the URL
driver.get("https://app.openhome.xyz")

# Log in
driver.find_element(By.NAME, "email").send_keys("mohsinalilkl@gmail.com")
driver.find_element(By.NAME, "password").send_keys("12345678")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Navigate to Create Personality
driver.find_element(By.CSS_SELECTOR, "nav[class='navbar-container'] button[class='create-nav-btn flexCenter']").click()
driver.find_element(By.CSS_SELECTOR, "div[class='ReactModalPortal'] button:nth-child(1) img:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR, "div[class='ReactModalPortal'] div[class='flexCenter'] button:nth-child(1)").click()

# Fill in the form
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Name']").send_keys("Testing_Personality")
driver.find_element(By.CSS_SELECTOR, "textarea[placeholder='Marketplace information']").send_keys("This is the market information")

# Upload the image
upload_path = r"D:\Upload media\Babar.jpg"
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Drag or choose and image to upload']").send_keys(upload_path)

driver.find_element(By.CSS_SELECTOR,"button[class='add-trigger-word-btn']").click()
driver.find_element(By.CSS_SELECTOR,"input[title='Key Tags']").send_keys("Triger word for test")
driver.find_element(By.CSS_SELECTOR,"section:nth-child(2) h2:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR,"textarea[placeholder='Description']").send_keys("This is the description for the testing personality")
driver.find_element(By.XPATH,"//label[normalize-space()='Publish Personality']").click()
driver.find_element(By.CSS_SELECTOR,"div[class='chakra-stack css-j8rple'] div:nth-child(1)").click()
driver.find_element(By.XPATH,"//button[normalize-space()='SAVE PERSONALITY']").click()

# Keep browser open
input("Press Enter to close the browser...")
driver.quit()

