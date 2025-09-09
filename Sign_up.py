from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--start-maximized")


# Automatically download and use the correct Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)
driver.get("https://app.openhome.xyz")

# Click on Sign Up
driver.find_element(By.XPATH, "//body/div[@id='root']/div[contains(@class,'flexCenter')]/div[contains(@class,'auth-container')]/div/button[1]").click()

# Fill out sign-up form
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Choose a unique username']").send_keys("Algoryc-QA")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Your email address']").send_keys("QA_Engineer@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Your first name']").send_keys("Algoryc")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Your last name']").send_keys("QA")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Choose a password']").send_keys("12345678")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Confirm your password']").send_keys("12345678")

# Wait for iframe and switch to reCAPTCHA
time.sleep(2)
iframe = driver.find_element(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
driver.switch_to.frame(iframe)

# Click the reCAPTCHA checkbox
driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()

# Switch back to main content
driver.switch_to.default_content()

# Wait a bit (in case of additional challenges)
time.sleep(10)

# Try submitting form again (if needed after CAPTCHA success)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Keep browser open until user presses Enter
input("Press Enter to close the browser...")
driver.quit()


# # Final wait to observe result
# time.sleep(5)

# driver.quit()
