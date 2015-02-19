import sys
from fetchArtist import fetchArtistId, fetchArtistInfo
from fetchAlbums import fetchAlbumIds, fetchAlbumInfo
from csvUtils import writeArtistsTable, writeAlbumsTable
from barChart import plotBarChart

if __name__ == '__main__':
    artist_names = sys.argv[1:]
    print "input artists are ", artist_names
    # YOUR CODE HERE
    artist_id_list = []
    artist_info_list = []
    album_id_list = []
    album_info_list = []
    for name in artist_names:
        artist_id_list.append(fetchArtistId(name))
    print artist_id_list
    for artist_id in artist_id_list:
        artist_info_list.append(fetchArtistInfo(artist_id))
    print artist_info_list
    for artist_id in artist_id_list:
        album_id_list.append(fetchAlbumIds(artist_id))
    print album_id_list
    for album_id in album_id_list:
        album_info_list.append(fetchAlbumInfo(album_id))
    print album_info_list

    writeArtistsTable(artist_info_list)
    writeAlbumsTable(album_info_list)
    plotBarChart()




    

