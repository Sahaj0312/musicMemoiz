import flask
from flask import jsonify
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy



app = flask.Flask(__name__)
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='f45fde97fecd49eabaf110129ebd394e', client_secret='725827c29b5a498f83d9e7e8bfa1754f'))
pl_id = 'https://open.spotify.com/playlist/2hRCvt3PvP7TlG47Ciyc2N?si=2cd7bbb2b8214a92'
offset = 0

names = []
aN = []
imgs = []
links = []


def song(playlist):
    response = sp.playlist_tracks(playlist, fields=None, limit=100, offset=0, market=None, additional_types=('track', ))

    for item in response['items']:
        track = item['track']
        title = track['name']
        names.append(title)
        artist = track['artists'][0]['name']
        img = track['album']['images'][1]['url']
        link = track['external_urls']['spotify']
        imgs.append(img)
        aN.append(artist)
        links.append(link)

    #index = random.randint(0,len(names)-1)
    nm = names
    ar = aN
    im = imgs
    ln = links

    return jsonify({
            "song": nm,
            "artist": ar,
            "image": im,
            "link": ln
            })


@app.route("/", methods=['GET'])
def home():
    return jsonify({"text": "yerrrrrrrr"})

@app.route("/rec", methods=['GET'])
def main():
    try:
        response = song(pl_id)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except KeyError:
        response = 'Invalid'
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
   


if __name__ == '__main__':
    app.run(debug=True)
