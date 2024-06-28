import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# import pprint

URL = 'https://www.billboard.com/charts/hot-100/'
CLIENT_ID = 'b16d9c8c343f4b2798fc9d5f2e54503c'
CLIENT_SECRET = '21196541106e475b8a3cd053e464beef'
REDIRECT_URL = 'http://example.com'
USER_NAME = 'gf19zn98cxt63xickq9spaira'

date = input('Which date do you want to travel to? Enter in this formate YYYY-MM-DD: ')
URL += date

response = requests.get(url=URL)
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

all_title_tags = soup.select(selector='ul li ul li h3')

song_names = [tag.getText().strip() for tag in all_title_tags]

year = date.split('-')[0]

scope = "playlist-modify-private"


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        show_dialog=True,
        cache_path="token.txt",
        username=USER_NAME,
    )
)

user_id = sp.current_user()['id']
song_uris = []

for song in song_names:
    result = sp.search(f'track:{song} year:{year}', type='track')

    try:
        song_uris.append(result['tracks']['items'][0]['uri'])
    except IndexError:
        print(f'Song: "{song}" does not exist in Spotify. Skipped!')


playlist_id = sp.user_playlist_create(
    user=user_id,
    name=f'{date} Billboard 100',
    public=False,
    description="joe mom's playlist"
)

playlist_id = playlist_id['id']


sp.playlist_add_items(playlist_id, song_uris)

print('Playlist created Successfully!')
