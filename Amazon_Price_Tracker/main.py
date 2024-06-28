import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

EMAIL = 'joemom7860@gmail.com'
PASSWORD = 'vgrumgyfhuwjooov'
TO_ADDR = 'omg.its.muhid@gmail.com'
URL = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
HEADER = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
    "Accept-Language": "en-US,en;q=0.5",
    'upgrade-insecure-requests': '1',
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "cross-site",
    "sec-fetch-user": "?1",
    # 'referer': 'https://www.amazon.com/',
}

response = requests.get(url=URL, headers=HEADER)

scraped_site = response.text

soup = BeautifulSoup(scraped_site, 'lxml')
price = float(soup.find(name='span', class_='a-offscreen').getText().split('$')[1])

if price < 100:
    with SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=TO_ADDR,
            msg="Subject: Joe is Back \n\n"
                f"Price is {price}. BUY NOW!"
        )

print('PROGRAM_END: SUCCESSFULL')