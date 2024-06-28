from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os


URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3621399760&distance=25.' \
      '0&f_AL=true&geoId=101022442&keywords=python%20developer'
driver_path = 'C:/Development/chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)
driver.get(URL)

# Signing In
sign_in_btn = driver.find_element(By.LINK_TEXT, 'Sign in')
sign_in_btn.click()

username_input = driver.find_element(By.ID, 'username')
username_input.send_keys('joemom7860@gmail.com')

password_input = driver.find_element(By.ID, 'password')
password_input.send_keys(os.getenv('password'))

password_input.send_keys(Keys.ENTER)
time.sleep(30)

# Applying
# apply_btn = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card button')
apply_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
apply_btn.click()
time.sleep(10)

# mobile_input = driver.find_element(By.CSS_SELECTOR, '#ember330 input')
# mobile_input = driver.find_element(By.CSS_SELECTOR, '#ember330 . artdeco-text-input--input')
mobile_input = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3621399760-90864093-phoneNumber-nationalNumber"]')
mobile_input.send_keys('03310648226')
time.sleep(5)

next_btn = driver.find_element(By.CSS_SELECTOR, '.pv4 button')
next_btn.click()
time.sleep(5)

next_btn = driver.find_element(By.CSS_SELECTOR, '.pv4 .artdeco-button--primary')
next_btn.click()
time.sleep(5)

question_input = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-'
                                             'applyformcommon-easyApplyFormElement-3621399760-90864077-numeric"]')
question_input.send_keys('0')

question_input = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-'
                                               'applyformcommon-easyApplyFormElement-3621399760-90864061-numeric"]')
question_input.send_keys('0')

question_input = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-'
                                               'applyformcommon-easyApplyFormElement-3621399760-90864069-numeric"]')
question_input.send_keys('0')
time.sleep(5)

# review_btn = driver.find_element(By.XPATH, '//*[@id="ember347"]')
review_btn = driver.find_element(By.CSS_SELECTOR, '.pv4 .artdeco-button--primary')
review_btn.click()
time.sleep(5)

submit_btn = driver.find_element(By.CSS_SELECTOR, '.pv4 .artdeco-button--primary')
submit_btn.click()
time.sleep(5)

time.sleep(100)
driver.quit()
