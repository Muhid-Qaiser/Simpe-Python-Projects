from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = 'C:/Development/chromedriver.exe'

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get('http://secure-retreat-92358.herokuapp.com/')

fname = driver.find_element(By.NAME, 'fName')
lname = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')
# submit = driver.find_element(By.CLASS_NAME, 'btn-block')
submit = driver.find_element(By.CSS_SELECTOR, 'form button')

fname.send_keys('Muhid')
lname.send_keys('Qaiser')
email.send_keys('email@gmail.com')
submit.click()

time.sleep(5)
