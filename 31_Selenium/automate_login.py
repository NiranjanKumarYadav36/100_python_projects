from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)


driver.get('https://the-internet.herokuapp.com/login')

username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located('userName'))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located('password'))
login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located('#login'))

username_field.send_keys('')
password_field.send_keys('')

WebDriverWait(driver, 10).until(EC.element_to_be_clickable(login_button))
login_button.click()

WebDriverWait(driver, 10).until(EC.title_contains('DEMOQA'))

input("press Enter to close the browser")

driver.quit()

