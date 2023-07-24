from flask import Flask, request, jsonify
from flask_cors import CORS
import SpotifyAPI
import ScoreAnalysis

app = Flask(__name__)
CORS(app)

finalScore = 0

@app.route('/textbox/submit', methods=['POST'])
def submitFeelings():
    global finalScore
    data = request.get_json()
    feelings = data['text']
    finalScore = ScoreAnalysis.getFinalScore(feelings)
    response_feeling = "Score Analysis: " + str(finalScore)
    print(response_feeling)
    return jsonify(response=response_feeling)

@app.route('/artistbox/submit', methods=['POST'])
def submitArtist():
    global finalScore
    data = request.get_json()
    artist = data['text']
    
    access_token = SpotifyAPI.get_token()
    artist_id = SpotifyAPI.artistID(access_token, artist)
    print(artist_id)
    audio_analysis = ScoreAnalysis.soundFeatures(finalScore)
    songRecs = SpotifyAPI.getSongRecommendations(access_token, artist_id, audio_analysis.getDancability(), audio_analysis.getEnergy(),
                                                audio_analysis.getLiveness(), audio_analysis.getValence(), audio_analysis.getTempo())
    
    song1 = [songRecs['tracks'][0]['name'], songRecs['tracks'][0]['artists'][0]['name'], songRecs['tracks'][0]['album']['images'][0]['url']]
    song2 = [songRecs['tracks'][1]['name'], songRecs['tracks'][1]['artists'][0]['name'], songRecs['tracks'][1]['album']['images'][0]['url']]
    song3 = [songRecs['tracks'][2]['name'], songRecs['tracks'][2]['artists'][0]['name'], songRecs['tracks'][2]['album']['images'][0]['url']]
    
    top3Array = [song1, song2, song3]       #Top 3 Rec song array with song name, artist name, and pic url
        
    return jsonify(response=top3Array)

if __name__ == '__main__':
    app.run()
