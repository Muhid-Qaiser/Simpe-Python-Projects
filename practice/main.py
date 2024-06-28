import requests
from bs4 import BeautifulSoup


response = requests.get(url='https://news.ycombinator.com/')

web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')
article_tag = soup.find_all(name='a', rel="noreferrer")
article_texts = []
article_links = []

for article in article_tag:
    article_texts.append(article.getText())
    article_links.append(article.get('href'))

article_score = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

print(article_texts)
print(article_links)
print(article_score)

highest_score = max(article_score)

highest_index = article_score.index(highest_score)
print(article_texts[highest_index])
print(article_links[highest_index])
