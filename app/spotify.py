import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = 'f9b92a146a3b4a4b90c558b23c82b918'
CLIENT_SECRET = '03c964ed7eab4e739f4ce68c133b8c66'
REDIRECT_URI = 'https://google.com'  # Use this for local testing

class SpotifyClient:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope="user-read-currently-playing"
        ))

    def get_currently_playing(self):
        current = self.sp.current_user_playing_track()
        if current and current.get('item'):
            return {
                'song': current['item']['name'],
                'artist': ', '.join([artist['name'] for artist in current['item']['artists']]),
                'album': current['item']['album']['name'],
                'is_playing': current['is_playing'],
                'progress_ms': current['progress_ms'],
                'duration_ms': current['item']['duration_ms'],
                'album_image': current['item']['album']['images'][0]['url'] if current['item']['album']['images'] else None,
                'external_url': current['item']['external_urls']['spotify']
            }
        return None

if __name__ == "__main__":
    client = SpotifyClient()
    print(client.get_currently_playing())
