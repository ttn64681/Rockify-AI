# Rockify AI
## Takes a user’s Spotify playlist to curate a new “Rockified” playlist, comprised of rock songs that are similar in lyrics, mood, and genre of the original user playlist.

Documentation: https://docs.google.com/document/d/16wMS2wS27Scacl2JkOjbNaHnDmn-ZD4y-D8es9u-OQA/edit?usp=sharing

# 1️⃣ Clone the repository
git clone https://github.com/ttn64681/Rockify-AI
cd your-repo

# 2️⃣ Create & activate a virtual environment
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate     # Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Set up environment variables (create .env file)
touch .env  # macOS/Linux
echo "SPOTIFY_CLIENT_ID=your-client-id-here" >> .env
echo "SPOTIFY_CLIENT_SECRET=your-client-secret-here" >> .env
echo "SPOTIFY_REDIRECT_URI=http://localhost:8000/callback" >> .env

# 5️⃣ Run the FastAPI backend
uvicorn backend:app --reload

# 6️⃣ (Not yet implemented) Run Streamlit UI
streamlit run frontend.py
