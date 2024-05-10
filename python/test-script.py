import pandas as pd

# Create a sample DataFrame
sample_df = pd.read_csv("files/table_test1.csv")
print(sample_df.head())
sample_df.columns
'''sample_df.columns
Index(['result', 'table', '_start', '_stop', '_time', '_value', '_field',
       '_measurement', 'building', 'floor', 'measuring', 'name'],
      dtype='object')'''

meter_data = {
    "name": "meter 2",
    "data": []
}

for index, row in sample_df.iterrows():
    data_point = {
        "time": row["_time"],
        "current_a": row["_value"],
        "current_b": row["current_b"],
        "kwh_t": row["kwh_t"]
    }
    meter_data["data"].append(data_point)


#test
    {
    "name": "values in name column",
    "data": [
    {
        "time": "time group 1 in time column",
        "value1 in field column": value in values column in the same row with value1 in field column,
        "value2 in field column": value in values column in the same row with value2 in field column,
        "value3 in field column": value in values column in the same row with value3 in field column,
        "value4 in field column": value in values column  in the same row with value4 in field column
    },
    {
        "time": "time group 2 in time column",
        "value5 in field column": value in values column in the same row with value5 in field column,
        "value6 in field column": value in values column in the same row with value6 in field column,
        "value7 in field column": value in values column in the same row with value7 in field column,
        "value8 in field column": value in values column  in the same row with value8 in field column
    }
    ]
    }

