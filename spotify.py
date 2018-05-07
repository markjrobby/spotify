import requests
import json
import pandas as pd
import sys

reload(sys)
sys.setdefaultencoding('utf8')

#recursively get all the metadata for each Spotify track
def recurseTracks(spotifyUrl): 
    flag = True
    while flag == True:
        response = requests.get(spotifyUrl, headers=headers)
        blob = response.content
        data = json.loads(blob)
        contents = data["items"]

        #only interested in Track Title, Artist Name, Album Name, ISRC Number
        for i in range(0, len(contents)):
            trackTitle = DictQuery(contents[i]).get("track/name")
            artist = DictQuery(contents[i]).get("track/artists/name")
            album = DictQuery(contents[i]).get("track/album/name")
            isrc = DictQuery(contents[i]).get("track/external_ids/isrc")
            trackTitles.append(trackTitle)
            artists.append(artist)
            albums.append(album)
            isrcs.append(isrc)

        if data["next"] is not None:
            return recurseTracks(data["next"])
        else:
            flag = False
            break

#helper function to retrive data within nested JSON
class DictQuery(dict):
    def get(self, path, default = None):
        keys = path.split("/")
        val = None
        for key in keys:
            if val:
                if isinstance(val, list):
                    val = [ v.get(key, default) if v else None for v in val]
                else:
                    val = val.get(key, default)
            else:
                val = dict.get(self, key, default)
            if not val:
                break
        return val



tokenID = raw_input('Enter OAuth Token:')
userID = raw_input('Enter Spotify UserID:')
playlistID = raw_input('Enter Spotify Playlist ID:')
url = 'https://api.spotify.com/v1/users/' + userID + '/playlists/' + playlistID + '/tracks'


#headers required for Spotify API
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + tokenID,
}

#creates pandas dataframe with columns
df = pd.DataFrame()
trackTitles = []
artists = []
albums = []
isrcs = []

#call Spotify API
recurseTracks(url)

#store data in its corresponding columns
df["Track Title"] = trackTitles
df["Artist"] = artists
df["Album"] = albums
df["ISRC"] = isrcs

#save to csv
df.to_csv("Spotify.csv")

