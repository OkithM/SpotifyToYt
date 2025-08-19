import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Your credentials from the Spotify Developer Dashboard
SPOTIPY_CLIENT_ID = 'YOUR_SPOTIFY_CLIENT_ID'
SPOTIPY_CLIENT_SECRET = 'YOUR_SPOTIFY_CLIENT_SECRET'
SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:8888/callback' # This should match the URI in your Spotify app settings
PLAYLIST_ID = 'YOUR_SPOTIFY_PLAYLIST_ID' # The ID of the playlist you want to get songs from


# The scope defines the permissions your app needs.
# 'playlist-read-private' allows reading a user's private playlists.
scope = "playlist-read-private"

# Set up the authentication manager
sp_oauth = SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=scope
)

# Create a Spotify API client instance
sp = spotipy.Spotify(auth_manager=sp_oauth)

try:
    # Get the playlist tracks. The 'fields' parameter helps limit the response data
    # to only what you need, which is more efficient.
    results = sp.playlist_items(PLAYLIST_ID, fields='items.track.name,items.track.artists.name,next')
    
    # Store the names in a list
    song_names = []
    
    # Loop through the results and extract the song and artist names
    for item in results['items']:
        track = item['track']
        song_name = track['name']
        artist_name = track['artists'][0]['name']  # Get the primary artist
        song_names.append(f"{song_name} by {artist_name}")

    # Handle pagination for playlists with more than 100 songs
    while results['next']:
        results = sp.next(results)
        for item in results['items']:
            track = item['track']
            song_name = track['name']
            artist_name = track['artists'][0]['name']
            song_names.append(f"{song_name} by {artist_name}")
            
    # Print the list of song names
    for name in song_names:
        print(name)
        
except spotipy.SpotifyException as e:
    print(f"An error occurred: {e}")
except IndexError:
    print("Could not retrieve artist or song name from one or more tracks.")