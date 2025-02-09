import os
import base64
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET:
    raise ValueError("Spotify credentials NOT set. Check your .env file or bash_profile.")

# =============================== #
# 🔹 GET ACCESS TOKEN MANUALLY 🔹 #
# =============================== #
def get_token():
    """
    Requests a new access token using Client Credentials Flow.
    Returns a valid access token.
    """
    url = "https://accounts.spotify.com/api/token"
    
    # Encode Client ID and Secret for Basic Auth
    auth_string = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
    auth_base64 = base64.b64encode(auth_string.encode()).decode()

    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}

    response = requests.post(url, headers=headers, data=data)
    json_result = response.json()

    if "access_token" not in json_result:
        raise Exception("❌ Failed to retrieve Spotify access token.")

    print(f"✅ Spotify Access Token: {json_result['access_token']}")  # <-- Print token
    return json_result["access_token"]


# Store the latest access token
SPOTIFY_ACCESS_TOKEN = get_token()

def get_auth_header():
    """
    Returns the Authorization header with the latest token.
    """
    return {"Authorization": f"Bearer {SPOTIFY_ACCESS_TOKEN}"}

# =============================== #
# 🔹 FETCH PLAYLIST DATA 🔹 #
# =============================== #
def getSpotifyPlaylist(playlistId):
    """
    Fetches tracks from a public Spotify playlist.
    Args:
        playlistId (str): The Spotify playlist ID.

    Returns:
        list: A list of song details (name, artist, track ID).
    """
    try:
        print(f"🔍 Fetching playlist: {playlistId}")

        url = f"https://api.spotify.com/v1/playlists/{playlistId}/tracks"
        headers = get_auth_header()

        response = requests.get(url, headers=headers)
        results = response.json()

        if "items" not in results:
            print(f"⚠️ Spotify API Error: {results}")
            return []

        songs = []
        for song in results["items"]:
            track = song["track"]
            if track:
                songs.append({
                    "name": track["name"],
                    "artist": track["artists"][0]["name"],
                    "id": track["id"]
                })

        if not songs:
            print("⚠️ No songs found in this playlist.")

        return songs
    
    except Exception as e:
        print(f"❌ Error fetching playlist: {e}")
        return []
