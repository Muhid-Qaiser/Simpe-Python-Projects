from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 40.00
PROMISED_UP = 40.00
EMAIL = 'joemom7860@gmail.com'
PASSWORD = 'joe123mom!@#'
DRIVER_PATH = 'C:/Development/chromedriver.exe'


class InternetSpeedTwitterBot:

    def __init__(self):
        self.up = 0
        self.down = 0
        self.driver = webdriver.Chrome(service=Service(DRIVER_PATH))

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        go_btn = self.driver.find_element(By.CLASS_NAME, 'start-text')
        go_btn.click()
        time.sleep(40)

        down_speed = self.driver.find_element(By.CLASS_NAME, 'download-speed')
        self.down = float(down_speed.text)

        up_speed = self.driver.find_element(By.CLASS_NAME, 'upload-speed')
        self.up = float(up_speed.text)

        # self.driver.quit()

    def tweet_at_provider(self):
        if PROMISED_UP > self.up and PROMISED_DOWN > self.down:
            time.sleep(5)
            self.driver.get("https://twitter.com/login")
            time.sleep(10)

            email_input = self.driver.find_element(By.NAME, 'text')
            email_input.send_keys(EMAIL)
            email_input.send_keys(Keys.ENTER)
            time.sleep(20)

            password_input = self.driver.find_element(By.NAME, 'password')
            password_input.send_keys(PASSWORD)
            password_input.send_keys(Keys.ENTER)
            time.sleep(10)

            tweet_input = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
            tweet_input.send_keys(f'AYO MY INTERNET SPEED TRASH. I WAS PROMISED {PROMISED_UP} upload and'
                                  f'{PROMISED_DOWN} download speed but am getting {self.up} upload and'
                                  f'{self.down} download speed. THIS IS ALL YOUR FAULT ERMITZ.')

            # tweet_btn = self.driver.find_element(By.CLASS_NAME, 'r-lrvibr')
            tweet_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                           'div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div'
                                                           '[2]/div[2]/div/div/div[2]/div[3]')
            tweet_btn.click()

            time.sleep(20)
            self.driver.quit()
