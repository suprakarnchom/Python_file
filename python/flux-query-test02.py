import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "2iDTxJVR-lZI20WI3yUnQno4uFu94yV5ZD873WAxXvaUnx7vX77OCyr-YsdMCCGfhIjfw1Vr5Y09Nfka67kFEA=="
org = "MEA"
url = "http://10.46.25.123:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)


fields = "fields" # "all"

def meter_name(name,fields,from_,to_,limit):
    query = f'''
    from(bucket: "test")
    |> range(start: {from_}, stop: {to_})
    |> filter(fn: (r) => r["_measurement"] == "power_meter")
    '''
    if name != "all":
        query += f'''
        |> filter(fn: (r) => r["name"] == "{name}")
        '''
    if fields != ["all"]:
        # Add a filter for each field
        field_filters = []
        for field in fields:
            field_filters.append(f'r["_field"] == "{field}"')
        field_filters_str = " or ".join(field_filters)
        query += f'|> filter(fn: (r) => {field_filters_str})'

    query += f'''
    |> aggregateWindow(every: 15m, fn: mean, createEmpty: false)
    |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
    '''
    if limit is not None:
        query += f'|> limit(n: {limit})'

    return query

query = meter_name("all",["all"],1706500369,1711818000,None)
query_api = client.query_api()
df_meter = query_api.query_data_frame(org=org, query=query)

import pandas as pd

print(df_meter)
df_meter['name'].unique()
df_meter['_time'].unique()
df_meter['_field'].unique()
df_meter.columns
# view sorted columns _time
df_meter['_time'].sort_values(ascending=False)
# df_meter['name'].unique()

# 10:23 power_meter index
# 9 name index

## solution from chatgpt
def df_meter_to_dict(df, file_name):
    import pandas as pd
    import json

    # Initialize an empty dictionary to hold data for all meters
    all_meter_data = {}

    # Group DataFrame by "name" and "_time" and iterate through each group
    for (name, time_group), group_df in df.groupby(['name', '_time']):
        # If the meter name doesn't exist in all_meter_data, create an empty list for it
        if name not in all_meter_data:
            all_meter_data[name] = []
        
        # Initialize an empty dictionary for the group data
        group_dict = {"time": str(time_group)}
        
        # Iterate through each row in the group
        for _, row in group_df.iterrows():
            # Use column index 10:23 as the key and the value as the value
            for col in range(10, min(24, len(row))):  # Ensure column index doesn't exceed row length
                group_dict[df.columns[col]] = row[col]
        
        # Append the group_dict to the list for the current meter
        all_meter_data[name].append(group_dict)

    # Write data for all meters to the file
    with open(file_name, 'w') as f:
        # Iterate over each meter's data and write it to the file
        for meter_name, meter_data in all_meter_data.items():
            # Create a dictionary containing meter name and its data
            meter_dict = {"name": meter_name, "data": meter_data}
            # Convert the dictionary to JSON string with indentation and write it to the file
            json_string = json.dumps(meter_dict, indent=4)
            f.write(json_string)
            f.write('\n')  # Add a newline for separation between meter data

# Call the function with the DataFrame and file name
df_meter_to_dict(df_meter, 'output/dict_field_meter_all-02.txt')
