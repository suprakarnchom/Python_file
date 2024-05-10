import pandas as pd

df_field = pd.read_csv('files/table_test-time03.csv')
df_field.head()
df_field.info()
df_field_meter1 = df_field[df_field['name'] == 'meter 1']
df_field_meter1.head()

dict_field_meter1 = {
    "name": df_field_meter1['name'].iloc[0],
    "data": []
}

# group DataFrame by "name" and "_time" and iterate through each group
for (name, time_group), group_df in df_field_meter1.groupby(['name', '_time']):
    # initialize an empty dictionary for the group data
    group_dict = {"time": str(time_group)}
    
    # iterate through each row in the group
    for _, row in group_df.iterrows():
        # use column index 11:23 as the key and the value as the value
        for col in range(11, 24):  # 24 is exclusive, so it will loop till 23
            group_dict[df_field.columns[col]] = row[col]
    
    # append the group_dict to the data list in dict_field_meter1
    dict_field_meter1["data"].append(group_dict)

# print the resulting dictionary
print(dict_field_meter1)



import json
# Convert the dictionary to a JSON string with indentation
json_string = json.dumps(dict_field_meter1, indent=4)

# Write the formatted JSON string to a file
with open('dict_field_meter1-02.txt', 'w') as f:
    f.write(json_string)