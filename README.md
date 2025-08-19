
# Spotify to YouTube Playlist Transfer

This project consists of two Python scripts that work together to transfer a playlist from Spotify to a YouTube playlist.

- **SpotifyToTxt.py** : Fetches all song titles and artists from a specified Spotify playlist and prints them to the console.

- **AddToYtPlaylist.py** : Reads a list of songs from a text file, searches for them on YouTube, and adds the first result to a designated YouTube playlist.

## Features

- **Spotify Integration** : Retrieves song names and artists from any public or private Spotify playlist.

- **YouTube Search** : Automatically searches for each song on YouTube to find a matching video.

- **Playlist Management** : Adds found videos to a YouTube playlist you specify.

- **Sequential Workflow** : The output of the first script provides the input for the second, creating a seamless transfer process.

## Prerequisites

- Python 3.x installed on your machine.

- A Spotify Developer account to create a new application and get API credentials.

- A Google Cloud Project with the YouTube Data API enabled.
## Installation

1. **Clone the Repository :**

```bash
git clone https://github.com/OkithM/SpotifyToYt
cd SpotifyToYt
```

2. **Install Dependencies :**

```bash
pip install spotipy google-api-python-client google-auth-oauthlib
```


## Setup and Configuration
1. **Spotify API Setup**
    - Go to the Spotify for Developers Dashboard.
    - Click "Create an App". Give it a name and a description.
    - Once created, find your Client ID and Client Secret.
    - In the app settings, click "Edit Settings" and add http://127.0.0.1:8888/callback as a "Redirect URI".
    - Open SpotifyToTxt.py and replace the placeholder values with your credentials and the Spotify playlist ID you want to transfer.
    ```bash
    SPOTIPY_CLIENT_ID = 'YOUR_SPOTIFY_CLIENT_ID'
    SPOTIPY_CLIENT_SECRET = 'YOUR_SPOTIFY_CLIENT_SECRET'
    SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:8888/callback' # This should match the URI in your Spotify app settings
    PLAYLIST_ID = 'YOUR_SPOTIFY_PLAYLIST_ID' # The ID of the playlist you want to get songs from
    ```

2. **Google YouTube Data API Setup**
    - Go to the Google Cloud Console.
    - Create a new project.
    - In the left-hand menu, navigate to "APIs & Services" > "Dashboard". Click "+ ENABLE APIS AND SERVICES" and search for "YouTube Data API v3". Enable it.
    - Navigate to "Credentials" > "CREATE CREDENTIALS" > "OAuth client ID".
    - Select "Desktop app" as the application type. Give it a name and click "Create".
    - A pop-up will appear with your client_id and client_secret. Click "DOWNLOAD CLIENT CONFIGURATION" and save the file as client_secret.json in the same directory as your Python scripts.
    - Open AddToYtPlaylist.py and replace the placeholder value with the YouTube playlist ID you want to add to.
    ```bash
    PLAYLIST_ID = "YOUR_YOUTUBE_PLAYLIST_ID" # The ID of the playlist you want to add to
    ```
## Usage
1. **Extract songs from Spotify :**
Run the SpotifyToTxt.py script. The first time you run it, a browser window will open for you to log in to your Spotify account and grant permissions.

```bash
python SpotifyToTxt.py > Songs.txt
```

This command will save the output of the script (a list of song names) into a new file named Songs.txt.

2. **Add songs to YouTube :**
With the Songs.txt file now populated, run the AddToYtPlaylist.py script. The first time you run this, a browser window will open for you to log in to your Google account and grant permissions.

```bash
python AddToYtPlaylist.py
```

The script will read each line from Songs.txt, search for a matching video, and add it to your YouTube playlist. The script will provide console feedback on its progress.


## Troubleshooting
- **"No video found for..." :** The YouTube search might not find a perfect match for the song query. You can manually check the song on YouTube to see if a playable video exists.

- **Authentication Errors :** Ensure your client_secret.json file is correctly named and in the same directory as the script. Also, double-check that your Client IDs and Client Secrets are copied correctly in both scripts.

- **"Could not retrieve artist or song name..." :** This may happen for certain tracks, like podcasts or specific user-uploaded content on Spotify.