import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Constants
CLIENT_ID = "client_id"
CLIENT_SECRET = "client_secrets"

# Function Definitions (if needed)

# User input
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Web scraping
URL = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
songs = soup.select(selector="li .o-chart-results-list__item h3")
song_titles = [song.getText().strip() for song in songs]

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Developer",
    )
)

# Spotify API requests
user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} - Billboard 100", public=False, collaborative=False, description=f"Billboard 100 on this date: {date}")

# Adding songs to the playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
