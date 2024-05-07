import csv
# read csv file to a list of dictionaries
with open('files/table_0.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]
print(data)

data.head()

import pandas as pd