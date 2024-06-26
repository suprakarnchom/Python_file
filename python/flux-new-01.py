import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import pandas as pd
import json
from rich import print
from collections import OrderedDict, defaultdict
token = "2iDTxJVR-lZI20WI3yUnQno4uFu94yV5ZD873WAxXvaUnx7vX77OCyr-YsdMCCGfhIjfw1Vr5Y09Nfka67kFEA=="
org = "MEA"
url = "http://10.46.25.123:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

def MeterReading():
    query = f'''
    from(bucket: "wat_liab")
        |> range(start: -30d)
        |> filter(fn: (r) => r["_measurement"] == "power_meter")
        |> aggregateWindow(every: 15m, fn: mean, createEmpty: false) 
        |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
    '''
    return query

query = MeterReading()
query_api = client.query_api()
df_meter = query_api.query_data_frame(org=org, query=query)

print(type(df_meter))
print(df_meter)


# tb  = df_meter[0]
# print(tb)
# tb.to_csv('output/table_meter/tb_meter1.csv', index=False)


df_meter.to_csv('output/site_info/sites01.csv', index=False)


# df_meter['device_id'].unique()
if type(df_meter) == pd.DataFrame:
    df_meter = [df_meter,]
    print(type(df_meter))
for df in df_meter:
    # Loop over each row in the DataFrame
    for index, row in df.iterrows():
        # Now you can access the data in each row
        # print(row)
        # print(type(row))
        dict1 = row.to_dict()
        print(dict1)
        #   ถ้ามีเดต้าในตารางแล้วข้าม continue 

      
