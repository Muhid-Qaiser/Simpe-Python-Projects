from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


FIVE_MINUTES = 60 * 5
FIVE_SECONDS = 5
chrome_driver_path = 'C:/Development/chromedriver.exe'

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get('http://orteil.dashnet.org/experiments/cookie/')


def check_price():
    for index in range(len(items_price) - 1, -1, -1):
        if current_money > items_price[index]:
            print(f"Purchased: {items_ids[index].strip('buy')} - ${items_price[index]}.")
            driver.find_element(By.ID, items_ids[index]).click()
            break


cookie = driver.find_element(By.ID, 'cookie')

items_tags = driver.find_elements(By.CSS_SELECTOR, '#rightPanel #store div')[:-1]
items_ids = [item.get_attribute("id") for item in items_tags]

items_price_tags = driver.find_elements(By.CSS_SELECTOR, '#rightPanel #store div b')[:-1]
items_price = [int(item.text.split()[-1].strip().replace(',', '')) for item in items_price_tags]

end_timer = time.time() + FIVE_MINUTES
timeout = time.time() + FIVE_SECONDS   # 5 seconds from now

while True:
    cookie.click()
    if timeout < time.time():

        items_price_tags = driver.find_elements(By.CSS_SELECTOR, '#rightPanel #store div b')[:-1]
        items_price = [int(item.text.split()[-1].strip().replace(',', '')) for item in items_price_tags]

        cost_upgrades = {}
        for n in range(len(items_price)):
            cost_upgrades[items_price[n]] = items_ids[n]

        current_money = driver.find_element(By.ID, 'money').text
        if ',' in current_money:
            current_money.replace(',', '')
        current_money = int(current_money)

        timeout = time.time() + FIVE_SECONDS

        check_price()

        if time.time() > end_timer:
            cps = driver.find_element(By.ID, 'cps').text
            print(cps)
            break


