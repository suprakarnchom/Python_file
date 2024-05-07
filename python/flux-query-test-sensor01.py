import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "2iDTxJVR-lZI20WI3yUnQno4uFu94yV5ZD873WAxXvaUnx7vX77OCyr-YsdMCCGfhIjfw1Vr5Y09Nfka67kFEA=="
org = "MEA"
url = "http://10.46.25.123:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)


sites = "sites" # "all"

def sensor_name(name,fields,from_,to_,limit):
    query = f'''
    from(bucket: "test")
    |> range(start: {from_}, stop: {to_})
    |> filter(fn: (r) => r["_measurement"] == "temp_sensor")
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
    |> group(columns: ["name"] , mode: "by")
    '''
    if limit is not None:
        query += f'|> limit(n: {limit})'

    return query

query = sensor_name("all",["all"],1706500369,1711818000,None)
query_api = client.query_api()
df_sensor = query_api.query_data_frame(org=org, query=query)

print(df_sensor)
type(df_sensor)
df_sensor.columns
df_sensor['name'].unique()

import pandas as pd 

def df_sensor_to_dict(df, file_name):
    import pandas as pd
    import json
    dict_field_sensor1 = {
    "name": df_sensor['name'].iloc[0],
    "data": []}

    # Group DataFrame by "name" and "_time" and iterate through each group
    for (name, time_group), group_df in df.groupby(["name", "_time"]):
        # initialize an empty dictionary for the group data
        group_dict = {"time": str(time_group)}

        # Iterate through each row in the group
        for _, row in group_df.iterrows():
            # Use column index 9:22 as the key and the value as the value
            for col in range(9, min(13, len(row))):  # Ensure column index doesn't exceed row length
                group_dict[df.columns[col]] = row[col]
        # append the group_dict to the data list in dict_field_sensor1
        dict_field_sensor1["data"].append(group_dict)

    # Convert the dictionary to a JSON string with indentation
    json_string = json.dumps(dict_field_sensor1, indent=4)

    # Write the formatted JSON string to a file
    with open(file_name, 'w') as f:
        f.write(json_string)

df_sensor_to_dict(df_sensor, 'output/dict_field_sensor1-03.txt')