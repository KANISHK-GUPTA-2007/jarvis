import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--headless")  # You can remove this to see the browser

driver = webdriver.Chrome(options=chrome_options)


driver.get('https://tts.5e7en.me/')

def speak_safe(text):
    element_to_click = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='text']"))
    )
    element_to_click.click()

    text_to_input = text
    element_to_click.send_keys(text_to_input)
    
    
    print(f'JARVIS : {text_to_input}')

    sleep_duration = min(0.3 + len(text) * 0.12, 60)


    button_to_click =  WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='button']"))
        )
    button_to_click.click()
    time.sleep(sleep_duration)

    element_to_click.clear()

