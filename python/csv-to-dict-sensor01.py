import pandas as pd

df_sensor = pd.read_csv('files/table_test-sensor01.csv')
df_sensor.head()
df_sensor.info()
df_sensor_sensor1 = df_sensor[df_sensor['name'] == 'temp_sensor_1']
df_sensor_sensor1.head()

dict_field_sensor1 = {
    "name": df_sensor_sensor1['name'].iloc[0],
    "data": []
}

# group DataFrame by "name" and "_time" and iterate through each group
for (name, time_group), group_df in df_sensor_sensor1.groupby(['name', '_time']):
    # initialize an empty dictionary for the group data
    group_dict = {"time": str(time_group)}
    
    # iterate through each row in the group
    for _, row in group_df.iterrows():
        # use column index 9:12 as the key and the value as the value
        for col in range(9, 13):  # 14 is exclusive, so it will loop till 13
            group_dict[df_sensor.columns[col]] = row[col]
    
    # append the group_dict to the data list in dict_field_sensor1
    dict_field_sensor1["data"].append(group_dict)

# print the resulting dictionary
print(dict_field_sensor1)



import json
# Convert the dictionary to a JSON string with indentation
json_string = json.dumps(dict_field_sensor1, indent=4)

# Write the formatted JSON string to a file
with open('dict_field_sensor1-01.txt', 'w') as f:
    f.write(json_string)