import unicodecsv as csv
import matplotlib.pyplot as plt

def getBarChartData():
    #Opens the csv files we've created and reads their rows and headers.
    f_artists = open('artists.csv')
    f_albums = open('albums.csv')

    artists_rows = csv.reader(f_artists)
    albums_rows = csv.reader(f_albums)

    artists_header = artists_rows.next()
    albums_header = albums_rows.next()

    artist_names = []
    
    #Creates a dictionary decade_dict. The keys are each decade between 1900 and 2020 (1900, 1910, 1920, etc.)
    #The values are the count of how many albums were released in that decade for all the artists in the csv file.
    #It gets this count by looking at the year the album was released and checking to see which two decade years it fell between
    #by looping through each decade between 1900 and 2020. If the release year is greater than or equal to the decade and less than
    #the next decade (the current decade + 10 years), then add 1 count to the value for that decade's key. 
    decades = range(1900,2020, 10)
    decade_dict = {}
    for decade in decades:
        decade_dict[decade] = 0
    
    #creates a list of artist_names by looping through each row in the artists.csv file 
    #and adding the name in that row to the artist_names list
    for artist_row in artists_rows:
        if not artist_row:
            continue
        artist_id,name,followers, popularity = artist_row
        artist_names.append(name)

    for album_row  in albums_rows:
        if not album_row:
            continue
        artist_id, album_id, album_name, year, popularity = album_row
        for decade in decades:
            if (int(year) >= int(decade)) and (int(year) < (int(decade) + 10)):
                decade_dict[decade] += 1
                break
    #Returns the decades betwen 1900 and 2020 as a list of x values. 
    #Returns the count of how many albums were released in each decade from the decades dictionary as a list of y values.
    #Also returns the artists names
    x_values = decades
    y_values = [decade_dict[d] for d in decades]
    return x_values, y_values, artist_names

def plotBarChart():
    x_vals, y_vals, artist_names = getBarChartData()
    
    #gets the values from the above function and plots them with "decades" on the x axis and "number of albums" on the y axis.
    #Sets the title of the plot as "Totals for {names of artists whose albums are considered}""
    #Displays the plot
    fig , ax = plt.subplots(1,1)
    ax.bar(x_vals, y_vals, width=10)
    ax.set_xlabel('decades')
    ax.set_ylabel('number of albums')
    ax.set_title('Totals for ' + ', '.join(artist_names))
    plt.show()


    
