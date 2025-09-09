from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--start-maximized")

service = Service("D:\Selenium Drivers\chromedriver-version-138.exe")

driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)

driver.get("https://app.openhome.xyz")

driver.find_element(By.NAME, "email").send_keys("mohsinalilkl@gmail.com")
driver.find_element(By.NAME, "password").send_keys("12345678")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

input("Press Enter to close the browser...")
driver.quit()
