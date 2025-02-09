"""
Testing Spotify API
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

sp_oauth = SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
    scope="playlist-read-private"
)

auth_url = sp_oauth.get_authorize_url()
print(f"Go to this URL to authorize: {auth_url}")

# After logging in, paste the redirect URL here:
redirect_response = input("Paste the full redirect URL here: ")

# Get access token
token_info = sp_oauth.get_access_token(redirect_response)
access_token = token_info['access_token']
print(f"Access Token: {access_token}")

# Use this token in your Spotify requests
sp = spotipy.Spotify(auth=access_token)
