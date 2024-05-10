
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "2iDTxJVR-lZI20WI3yUnQno4uFu94yV5ZD873WAxXvaUnx7vX77OCyr-YsdMCCGfhIjfw1Vr5Y09Nfka67kFEA=="
org = "MEA"
url = "http://10.46.25.123:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)


fields = "fields" # "all"

def build_query(fields):
    query = f'''
    from(bucket: "test")
    |> range(start: -10d)
    |> filter(fn: (r) => r["_measurement"] == "power_meter")
    '''

    if fields != all:
        query += f'''
        |> filter(fn: (r) => r["_field"] == "{fields}")
        '''
    
    query += f'''
    |> aggregateWindow(every: 15m, fn: mean, createEmpty: false)
    |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
    |> group(columns: ["name"] , mode: "by")
    '''

    return query

query = build_query(all)
query_api = client.query_api()
tables = query_api.query_data_frame(org=org, query=query)

print(tables)
type(tables)

import pandas as pd

tables.to_csv("files/table_test-time02.csv", index=False)

