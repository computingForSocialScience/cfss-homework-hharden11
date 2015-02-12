import requests
from datetime import datetime

def fetchAlbumIds(artist_id):
    """Using the Spotify API, take an artist ID and 
    returns a list of album IDs in a list
    """
    url = "https://api.spotify.com/v1/artists/" + artist_id + "/albums?market=US&album_type=album"
    print url
    req = requests.get(url)
    raw_data = req.json()
    return req.json()["items"][0]['id']
print fetchAlbumIds('0vYkHhJ48Bs3jWcvZXvOrP')

def fetchAlbumInfo(album_id):
    """Using the Spotify API, take an album ID 
    and return a dictionary with keys 'artist_id', 'album_id' 'name', 'year', popularity'
    """
    url = "https://api.spotify.com/v1/albums/" + album_id
    print url
    req = requests.get(url)
    raw_data = req.json()
    AlbumInfo_dict = {}
    AlbumInfo_dict["artist_id"] = raw_data["artists"][0]["id"]
    AlbumInfo_dict["album_id"] = raw_data["id"]
    AlbumInfo_dict["name"] = raw_data["name"]
    AlbumInfo_dict["year"] = raw_data["release_date"][0:4]
    AlbumInfo_dict["popularity"] = raw_data["popularity"]
    return AlbumInfo_dict
    print AlbumInfo_dict
print fetchAlbumInfo('0BTbgjERGPFlELxXy9BaSe')

