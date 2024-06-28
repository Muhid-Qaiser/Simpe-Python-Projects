from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


chrome_driver_path = 'C:/Development/chromedriver.exe'

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get('http://orteil.dashnet.org/experiments/cookie/')
current_money = 0

cookie = driver.find_element(By.ID, 'cookie')

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ds = [item.get_attribute("id") for item in items]

checker = driver.find_elements(By.CSS_SELECTOR, '#rightPanel #store div b')[:-1]

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

while True:
    cookie.click()

    #Every 5 seconds:
    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != '':
                cost = int(element_text.split('-')[1].strip().replace(',', ''))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ds[n]

        money_element = driver.find_element(By.ID, 'money').text
        if ',' in money_element:
            money_element = money_element.replace(',', '')
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        timeout = time.time() + 5

        # After 5 minutes stop the bot and check the cookies per second count.
        if time.time() > five_min:
            cookie_per_s = driver.find_element(By.ID, 'cps').text
            print(cookie_per_s)
            break
