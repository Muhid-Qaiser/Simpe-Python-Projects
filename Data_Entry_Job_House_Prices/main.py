from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

DRIVER_PATH = "C:/Development/chromedriver.exe"

GOOGLE_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLScowzykknfAWcurcD5RecMmy_' \
              'mtSbpxQ0X-Eh9Gwf5KroZXhw/viewform?usp=sf_link'
WEBSITE_URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22' \
              'usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-' \
              '122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22is' \
              'MapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%' \
              '7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afal' \
              'se%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22' \
              '%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Af' \
              'alse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3' \
              'A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'

driver = webdriver.Chrome(service=Service(DRIVER_PATH))
driver.get(WEBSITE_URL)

time.sleep(30)

link_list_tag = driver.find_elements(By.CSS_SELECTOR, '#grid-search-results ul li .property-card-data a')
link_list = [tag.get_attribute('href') for tag in link_list_tag]

address_list_tag = driver.find_elements(By.CSS_SELECTOR, '#grid-search-results ul li .property-card-data a address')
address_list = [tag.text for tag in address_list_tag]

price_list_tag = driver.find_elements(By.CSS_SELECTOR, '#grid-search-results ul li .property-card-data span .jLQjry')
price_list = [tag.text for tag in price_list_tag]

print(address_list)
print(price_list_tag)

time.sleep(10)

driver.quit()
