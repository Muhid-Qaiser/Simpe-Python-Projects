import os
import requests
import smtplib


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
PASSWORD = 'vgrumgyfhuwjooov'
EMAIL = 'joemom7860@gmail.com'

STOCKS_API_KEY = os.environ.get('STOCKS_API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    'apikey': STOCKS_API_KEY,
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK_NAME,
}

news_params = {
    'qInTitle': COMPANY_NAME,
    'language': 'en',
    'apiKey': NEWS_API_KEY,
}

up_down = None

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.json()['Time Series (Daily)']

closing_prices = [float(value['4. close']) for (key, value) in data.items()]
yesterday_closing_price = closing_prices[0]
day_before_yesterday_closing_price = closing_prices[1]

difference = abs(round(yesterday_closing_price - day_before_yesterday_closing_price, 2))

if difference > 0:
    up_down = '^'
else:
    up_down = 'v'

percentage = round((difference / day_before_yesterday_closing_price) * 100, 2)

if True:
    print('Get News')
    response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = response.json()['articles']
    three_articles = articles[:2]
    formatted_article = [f"Headline: {article['title']}. \nDescription: {article['description']}." for article in three_articles]

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        for article in formatted_article:
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs='omg.its.muhid@gmail.com',
                msg=f'\nTSLA: {up_down} {percentage}%. \n{article}'
            )
