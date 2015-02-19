
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import re
import sys
import csv

def fetchArtistId(name):
    """Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """
    url = "https://api.spotify.com/v1/search?q=" + name + "&type=artist"
    #print url
    req = requests.get(url)
    return req.json()["artists"]["items"][0]['id']
print fetchArtistId("Patti Smith")


def fetchArtistInfo(artist_id):
    """Using the Spotify API, takes a string representing the id and
    returns a dictionary including the keys 'followers', 'genres', 
    'id', 'name', and 'popularity'.
    """
    url = "https://api.spotify.com/v1/artists/" + artist_id
    #print url
    req = requests.get(url)
    raw_data = req.json()
    ArtistInfo_dict = {}
    ArtistInfo_dict["followers"] = raw_data["followers"]["total"]
    ArtistInfo_dict["genres"] = raw_data["genres"]
    ArtistInfo_dict["id"] = raw_data["id"]
    ArtistInfo_dict["name"] = raw_data["name"]
    ArtistInfo_dict["popularity"] = raw_data["popularity"]
    return ArtistInfo_dict
print fetchArtistInfo('0vYkHhJ48Bs3jWcvZXvOrP')
