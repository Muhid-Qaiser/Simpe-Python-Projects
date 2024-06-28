from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

DRIVER_PATH = 'C:/Development/chromedriver.exe'
SIMILAR_ACC = 'natgeotravel'
PASSWORD = 'joe123mom!@#'
EMAIL = 'joemom7860@gmail.com'


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(DRIVER_PATH))

    def login(self):
        self.driver.get(url='https://www.instagram.com/accounts/login/')
        time.sleep(5)

        email_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_input.send_keys(EMAIL)

        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(PASSWORD)
        time.sleep(2)

        password_input.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(10)

        search_btn = self.driver.find_elements(By.CSS_SELECTOR, '.x78zum5 a .x30kzoy')
        search_btn[2].click()
        time.sleep(5)

        search_input = self.driver.find_element(By.CSS_SELECTOR, '._amr8 input')
        search_input.send_keys(SIMILAR_ACC)
        time.sleep(5)

        account_btn = self.driver.find_elements(By.CSS_SELECTOR, '.xh8yej3 .x1nhvcw1 .xeuugli')
        account_btn[0].click()
        time.sleep(10)

        follower_btn = self.driver.find_element(By.CSS_SELECTOR, 'ul li .x1a2a7pz')
        follower_btn.click()
        time.sleep(10)

        # scroll_btn = self.driver.find_element(By.CSS_SELECTOR, 'div ._aano')
        # for _ in range(10):
        # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_btn)
        # time.sleep(5)

    def follow(self):
        follow_btns = self.driver.find_elements(By.CSS_SELECTOR, 'div ._aano button')
        # follow_btns = self.driver.find_elements(By.CSS_SELECTOR, 'li button')

        try:
            for btn in follow_btns:
                btn.click()
                time.sleep(2)
        except ElementClickInterceptedException:
            cancel_btn = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_8p"]/div/div/div[3]/div/div[2]'
                                                            '/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
            cancel_btn.click()

        # Or
        # for btn in follow_btns:
        #     if btn.text == 'Follow':
        #         btn.click()
        #     else:
        #         pass
