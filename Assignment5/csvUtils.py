import csv
from io import open

def writeArtistsTable(artist_info_list):
    """Given a list of dictionaries, each as returned from fetchArtistInfo(), write a csv file 'artists.csv' 
    with the following header: ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY"""
    f = open ('artists.csv','w',encoding='utf-8')
    f.write(u"ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY\n")
    for i in range(0,len(artist_info_list)):
        artist_dictionary = artist_info_list[i]
        ARTIST_ID = artist_dictionary['id']
        ARTIST_NAME = artist_dictionary['name']
        ARTIST_FOLLOWERS = artist_dictionary['followers']
        ARTIST_POPULARITY = artist_dictionary['popularity']
        f.write('"%s","%s","%s","%s" \n' %(ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY))
    f.close()
print writeArtistsTable([{'genres': [u'protopunk'], 'popularity': 63, 'followers': 75637, 'id': u'0vYkHhJ48Bs3jWcvZXvOrP', 'name': u'Patti Smith'}])

      
def writeAlbumsTable(album_info_list):
    """Given list of dictionaries, each as returned from the function fetchAlbumInfo(), write a csv file 'albums.csv'
    with the following header: ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY"""
    f = open ('albums.csv','w',encoding='utf-8')
    f.write(u"ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY\n")
    for i in range(0,len(album_info_list)):
        album_dictionary = album_info_list[i]
        ARTIST_ID = album_dictionary['artist_id']
        ALBUM_ID = album_dictionary['album_id']
        ALBUM_NAME = album_dictionary['name']
        ALBUM_YEAR = album_dictionary['year']
        ALBUM_POPULARITY = album_dictionary['popularity']
        f.write('"%s","%s","%s","%s","%s" \n' %(ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY))
    f.close()
print writeAlbumsTable([{'popularity': 23, 'artist_id': u'0vYkHhJ48Bs3jWcvZXvOrP', 'year': u'2008', 'name': u'The Coral Sea', 'album_id': u'0BTbgjERGPFlELxXy9BaSe'}])
