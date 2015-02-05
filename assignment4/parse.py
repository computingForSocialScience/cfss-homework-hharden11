import csv
import sys
import numpy
import matplotlib.pyplot as plt

def readCSV(filename):
    '''Reads the CSV file `filename` and returns a list
    with as many items as the CSV has rows. Each list item 
    is a tuple containing the columns in that row as stings.
    Note that if the CSV has a header, it will be the first
    item in the list.'''
    with open(filename,'r') as f:
        rdr = csv.reader(f)
        lines = list(rdr)
    return(lines)

### enter your code below
hp_permits = readCSV("permits_hydepark.csv")
lat_list = []
lng_list = []
for i in range(1,len(hp_permits)):
		lat_list.append(float(hp_permits[i][128]))
		lng_list.append(float(hp_permits[i][129]))

def get_avg_latlng(hp_permits):
	lat_mean = numpy.mean(lat_list)
	lng_mean = numpy.mean(lng_list)
	print(lat_mean,lng_mean)


def zip_code_barchart(x):
	zip_list = []
	zip_list_clean = []
	zip_dict = {}
	for i in range(1,len(hp_permits)):
		zip_list.append(hp_permits[i][28])
		zip_list.append(hp_permits[i][35])
		zip_list.append(hp_permits[i][42])
		zip_list.append(hp_permits[i][49])
		zip_list.append(hp_permits[i][56])
		zip_list.append(hp_permits[i][63])
		zip_list.append(hp_permits[i][70])
		zip_list.append(hp_permits[i][77])
		zip_list.append(hp_permits[i][84])
		zip_list.append(hp_permits[i][91])
		zip_list.append(hp_permits[i][98])
		zip_list.append(hp_permits[i][105])
		zip_list.append(hp_permits[i][112])
		zip_list.append(hp_permits[i][119])
		zip_list.append(hp_permits[i][126])
	for i in zip_list:
		zip_list_clean.append(i[:5])
		if i == '':
			zip_list_clean.remove(i)
	print zip_list_clean
	for i in zip_list_clean:
	    if i in zip_dict.keys():
	        zip_dict[i] = zip_dict[i]+1
	    else:
	        zip_dict[i] = 1
	print(zip_dict)
	fig = plt.figure(figsize=(5.5,3),dpi=300)
	plt.bar(range(len(zip_dict)), zip_dict.values(), align='center')
	plt.xticks(range(len(zip_dict)), zip_dict.keys(),size=5)
	plt.title("Contractor Zip Codes in Hyde Park", fontsize = 10)
	fig.savefig("barchart.jpg")

#python parse.py hist
#python parse.py latlong
if sys.argv[1] == "latlong":
	get_avg_latlng(hp_permits)
elif sys.argv[1]  == "hist":
	zip_code_barchart(hp_permits)