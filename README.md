# Spotify Metadata Tool
A Python script that pull metadata from every track in a specified playlist through Spotify's Web API and stores it in a csv.

## Instructions
1. Clone the repo and create a virtualenv and activate it
2. Install the following packages using `pip`:
  - `pip install json`
  - `pip install requests` 
  - `pip install pandas`
  - `pip install sys` 
  
3. Get a Spotify OAuth Token (for a temporary token that only lasts at most an hour use this link: https://beta.developer.spotify.com/console/get-playlist-tracks/?user_id=spotify_espa%C3%B1a&playlist_id=21THa8j9TaSGuXYNBU5tsC&market=&fields=&limit=&offset=more)

4. Run `python spotify.py` and enter Spotify User ID, Spotify Playlist ID and the generated Spotify OAuth Token. The Spotify User ID (right after /user/) and Spotify Playlist ID (right after /playlist/) can be inferred in the Spotify url link of the playlist.

### Output:
1. Currently this script only outputs Track Name, Artist Name, Album Name and ISRC into the csv. However you can always modify the script to include or omit other data that is returned.
