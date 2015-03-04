import requests
import pandas as pd

def getRelatedArtists(artistID):
    """Using the Spotify Get an Artist's Related Artists API, take an individual artist's ID 
    and return the IDs of up to 20 related artists."""
    url = "https://api.spotify.com/v1/artists/" + artistID +"/related-artists"
    #print url
    req = requests.get(url)
    raw_data = req.json()
    related_artists_list = []
    for artist in raw_data["artists"]:
        related_artists_list.append(artist["id"])
    return related_artists_list
print getRelatedArtists("2mAFHYBasVVtMekMUkRO9g")

def getDepthEdges(artistID, depth):
    '''takes two arguments, an artist ID and an integer depth, and returns a 
    list of tuples representing the (directed) pairs of related artists'''
    original_list = getRelatedArtists(artistID)
    tuple_list = []
    for i in original_list:
        tuple_list.append((artistID,i))
    if depth == 1:
        return tuple_list
    else:
        for i in original_list:
            tuple_list.extend(getDepthEdges(i,depth-1))
        return tuple_list
print getDepthEdges("2mAFHYBasVVtMekMUkRO9g",2)

def getEdgeList(artistID, depth):
    '''takes the exact same arguments as getDepthEdges(), but returns the result 
    as a Pandas DataFrame with one row for each edge'''
    data = getDepthEdges(artistID,depth)
    df = pd.DataFrame(data)
    return df
print getEdgeList("2mAFHYBasVVtMekMUkRO9g",2)

def writeEdgeList(artistID, depth, filename):
    '''takes three arguments: an artist ID, a depth value, and a filename for output. 
    This function generates an edge list based on the parameters artistId and depth, 
    and writes that to a CSV file specified by the filename parameter'''
    df = getEdgeList(artistID, depth)
    df.to_csv(filename,index=False,quotechar='"')
print writeEdgeList("2mAFHYBasVVtMekMUkRO9g",2,"edges.csv")