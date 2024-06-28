from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = 'C:/Development/chromedriver.exe'

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

# python.org tings
driver.get('https://www.python.org/')

date_tags = driver.find_elements(By.CSS_SELECTOR, '.last time')
event_tags = driver.find_elements(By.CSS_SELECTOR, '.event-widget  ul[class="menu"] li a[href]')

dict = {}

for index in range(len(date_tags)):
    dict[index] = {
        'time': date_tags[index].text,
        'name': event_tags[index].text
    }

print(dict)

# driver.quit()


# print(price.get_attribute('placeholder'))
