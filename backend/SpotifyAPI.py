import requests
import base64
import ScoreAnalysis
from ScoreAnalysis import *

#Authorization parameters
client_id = "6c669516a1344c7e92731cd4da00cb07"
client_secret = "4fb4070102234dcabfab3899b9148c9b"

def get_token() :
    #Encode client credentials
    client_credentials = f"{client_id}:{client_secret}"
    base64_credentials = base64.b64encode(client_credentials.encode("utf-8")).decode("utf-8")
    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {base64_credentials}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(token_url, headers=headers, data=data)
    if response.status_code == 200:
        access_token = response.json()["access_token"]
        return access_token
    else:
        print("Failed to obtain access token. Error:", response.json())

def get_auth_header(token) :
    return {"Authorization": "Bearer " + token}

def artistID(token, name) :
    search_url = f"https://api.spotify.com/v1/search?q={name}&type=artist"
    headers = get_auth_header(token)
    result = requests.get(search_url, headers=headers)
    data = result.json()
    artist_id = data["artists"]["items"][0]["id"]
    return artist_id

def getSongRecommendations(token, artist, dancability, energy, liveness, valence, tempo) :
    recommendations_url = "https://api.spotify.com/v1/recommendations"
    headers = get_auth_header(token)
    params = {
        "limit": 3,
        "seed_artists": artist,
        "target_danceability": dancability,
        "target_energy": energy,
        "min_popularity": 40,
        "target_liveness": liveness,
        "target_valence": valence,
        "max_tempo": tempo
        }
    result = requests.get(recommendations_url, headers=headers, params=params)
    recommendations_data = result.json()
    return recommendations_data