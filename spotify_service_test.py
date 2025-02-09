# Spotipy - python library for Spotify Web API
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv


# For getting environment variables, where the
# Client ID and Client Secret was exported in ~./bash_profile
load_dotenv()

# Load API credentials from environment variables
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
#SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

# Allows reading the user's playlist
#scope = "playlist-read-private" 

if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET:
    raise ValueError("Spotify credentials NOT set. Check your .env file.")

# Authenticate using Spotify Client Credentials Flow
auth_manager = SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
)
sp = spotipy.Spotify(auth_manager=auth_manager)

print("🔍 Checking Spotify Access Token:")
print(sp.auth_manager.get_access_token(as_dict=False))

"""
Essentially retrieves a public playlist and
gets information from each song in order for
Rockify app to send that info to the AI services
(GPT-4 and Genius) to analyze and recommend
rock songs based on the playlist's songs' info.
"""
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

        url = f"https://api.spotify.com/v1/playlists/{playlistId}"
        headers = get_auth_header()

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"⚠️ API Error {response.status_code}: {response.json()}")
            return []

        results = response.json()

        if "tracks" not in results or "items" not in results["tracks"]:
            print("⚠️ No tracks found in response.")
            return []

        songs = []
        for song in results["tracks"]["items"]:
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
