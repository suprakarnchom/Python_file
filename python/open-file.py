import csv
with open('files/table_0.csv',mode='r') as infile:
    reader = csv.DictReader(infile)
    data = {row for row in reader}
type(data)
# convert data to dictionary
data = dict(data)

Def device_meters(site=”all”,building=”all”,floor=”all”)
		Return dict(meters=[])
# Use the function

import csv

def csv_to_dict('files/table_0.csv'):
    with open('files/table_0.csv', mode='r') as infile:
        reader = csv.DictReader(infile)
        data = [row for row in reader]
    return data

def device_meters('files/table_0.csv', site="all", building="all", floor="all"):
    data = csv_to_dict('files/table_0.csv')
    return dict(meters=data)

# Use the function
meters = device_meters('files/table_0.csv')