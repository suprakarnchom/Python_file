import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import pandas as pd
import json
from rich import print
from collections import OrderedDict, defaultdict
# import tqdm
from tqdm import tqdm
token = "2iDTxJVR-lZI20WI3yUnQno4uFu94yV5ZD873WAxXvaUnx7vX77OCyr-YsdMCCGfhIjfw1Vr5Y09Nfka67kFEA=="
org = "MEA"
url = "http://10.46.25.123:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

def SIteInfo_data():
    query = f'''
    from(bucket: "wat_liab")
        |> range(start: -30d)
        |> filter(fn: (r) => r["_measurement"] == "power_meter")
        |> aggregateWindow(every: 15m, fn: mean, createEmpty: false) 
        |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
        '''
    return query

query = SIteInfo_data()
query_api = client.query_api()
df_sites = query_api.query_data_frame(org=org, query=query)

print(type(df_sites))
print(df_sites)

# merge list of dataframes
df_sites = pd.concat(df_sites)

df_sites.to_csv('output/site_info/sites02.csv', index=False)
# count na values
print(df_sites.isna().sum())

# df_meter.to_csv('output/table_meter/tb_meter_kw_demand01.csv', index=False)


# df_meter['device_id'].unique()
if type(df_sites) == pd.DataFrame:
    df_sites = [df_sites,]
    print(type(df_sites))
for df in df_sites:
    # Loop over each row in the DataFrame 
        for index, row in tqdm(df.iterrows()):
            # Now you can access the data in each row by the column name
            dict1 = row.to_dict()
        #   ถ้ามีเดต้าในตารางแล้วข้าม continue 


      
