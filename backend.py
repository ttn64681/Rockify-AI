# FastAPI framework
from fastapi import FastAPI, HTTPException

# import functions from other py files
from spotify_service import getSpotifyPlaylist
# from ai_service import analyzeLyrics, recommendRockSongs
# from database import savePlaylist, getPastRecommendations

app = FastAPI()

# ============= API Endpoints ============= #

# FastAPI Home endpoint (root url '/')
@app.get("/")
def home():
    """
    This makes it so accessing the root URL of the app
    (starting the app) returns the following test message.
    """
    return {"message": "Rockify AI successfully starting!"}

# endpoint for 
@app.get("/analyze_playlist/")
def analyzePlaylist(playlistId: str):
    try:
        print(f"🔍 Analyzing playlist {playlistId}")
        # fetches songs from Spotify API
        songs = getSpotifyPlaylist(playlistId)

        if not songs:
            print("⚠️ No songs found or API error.")
            raise HTTPException(status_code=400, 
                                detail="Invalid playlist or no songs found.")
        
        return {"playlist": songs}


        # analyzes mood & recommends rock songs via OpenAI (GPT-4)
        #recommendations = recommendRockSongs(songs)
        # stores recommendations in MongoDB
        #savePlaylist(playlistId, recommendations)

        # returns recommended rock playlist JSON response

        #return {"playlist": recommendations}
    
    except Exception as e:
        # failed to process given playlist id (rip)
        print(f"Error in analyzePlaylist: {e}")
        raise HTTPException(status_code=500, detail="Failed to process playlist.........")

@app.get("/history/")
def history():
    # returns the past stored recommendations in MongoDB
    #return getPastRecommendations()
    return

# Run with: uvicorn backend:app --reload
# Essentially same as "Run app from backend module"