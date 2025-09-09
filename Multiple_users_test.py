import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def run_chrome_user(email, password):
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1
    })

    # Use webdriver_manager to auto-download and match ChromeDriver
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    messages = [
        "How to create Personality on openhome",
        "tell me about openhome",
        "tell me about ability creation",
        "tell me about life with ai "
    ]

    try:
        driver.implicitly_wait(10)
        driver.get("https://app.openhome.xyz")

        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

        driver.find_element(By.XPATH, "//li[@id='Openhome']").click()
        time.sleep(5)
        
        i = 0
        while True:
            message_input = driver.find_element(By.XPATH, "//input[@id='myInput']")
            send_button = driver.find_element(By.XPATH, "//button[@id='myBtn']")
            time.sleep(10)
            message = messages[i]
            message_input.clear()
            message_input.send_keys(message)
            send_button.click()
            print(f"[{email}] Sent: {message}")

            i = (i + 1) % len(messages)  # Loop through messages
            time.sleep(10)  # wait 10 seconds before next message

    except Exception as e:
        print(f"Chrome user {email} failed with error: {e}")
    # Browser stays open intentionally


users = [
    {"email": "mohsinalilkl@gmail.com", "password": "12345678"},
    {"email": "algorycQA@gmail.com", "password": "12345678"},
    {"email": "qaengineer6268@gmail.com", "password": "12345678"},
    {"email": "QA_Engineer@gmail.com", "password": "12345678"}
]

threads = []
for user in users:
    t = threading.Thread(target=run_chrome_user, args=(user["email"], user["password"]))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
