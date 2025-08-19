import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import sys

# The necessary scopes for managing playlists
scopes = ["https://www.googleapis.com/auth/youtube"]

# Add this line for better character handling
sys.stdout.reconfigure(encoding='utf-8')

# Your API credentials
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
CLIENT_SECRETS_FILE = "client_secret.json" # You'll need to download this from Google Console
PLAYLIST_ID = "YOUR_YOUTUBE_PLAYLIST_ID" # The ID of the playlist you want to add to

# The name of the file containing the list of songs
SONGS_FILE = "Songs.txt"

def get_authenticated_service():
    """Authenticates with the YouTube API and returns the service object."""
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes)
    credentials = flow.run_local_server(port=8080)
    return googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials)

def add_video_to_playlist(youtube, playlist_id, video_id):
    """Adds a video to a YouTube playlist."""
    request_body = {
        'snippet': {
            'playlistId': playlist_id,
            'resourceId': {
                'kind': 'youtube#video',
                'videoId': video_id
            }
        }
    }
    try:
        response = youtube.playlistItems().insert(
            part="snippet",
            body=request_body
        ).execute()
        print(f"✅ Successfully added video to playlist: {response['snippet']['title']}")
    except googleapiclient.errors.HttpError as e:
        print(f"❌ An error occurred when adding the video: {e}")

def search_for_video(youtube, query):
    """Searches for a video on YouTube and returns the first result's ID."""
    search_response = youtube.search().list(
        q=query,
        type="video",
        part="id,snippet",
        maxResults=1
    ).execute()

    if not search_response['items']:
        print(f"🔍 No video found for: {query}")
        return None
    
    video = search_response['items'][0]
    return video['id']['videoId']

if __name__ == "__main__":

    if not os.path.exists(CLIENT_SECRETS_FILE):
        print("Please download client_secret.json from the Google Cloud Console.")
        exit()

    if not os.path.exists(SONGS_FILE):
        print(f"Please create a file named {SONGS_FILE} and add one song per line.")
        exit()

    youtube = get_authenticated_service()

    with open(SONGS_FILE, 'r', encoding='utf-8') as f:
        for song_to_add in f:
            song_to_add = song_to_add.strip()
            if song_to_add:
                print(f"Searching for video: {song_to_add}")
                video_id = search_for_video(youtube, song_to_add)

                if video_id:
                    print(f"Video found, adding to playlist...")
                    add_video_to_playlist(youtube, PLAYLIST_ID, video_id)
                else:
                    print(f"Could not find a video to add for: {song_to_add}")
    
    print("\n✅ Finished processing all songs from the file.")