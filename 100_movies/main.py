import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')
movies_tags = soup.find_all(name='h3', class_='title')
movie_titles = [movie_tag.getText() for movie_tag in movies_tags]
movie_titles.reverse()

with open('movies.txt', 'a', encoding="utf-8") as movie_file:
    for movie in movie_titles:
        movie_file.write(movie + '\n')

