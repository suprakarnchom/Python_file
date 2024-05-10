'''df_meter1= df[df['name'] == 'meter 1']
df_meter1.head()
df_meter1['name'].unique()

dict_field_meter1 = {
    "name": df_meter1['name'].iloc[0],
    "data": []
}

# group DataFrame by "name" and "_time" and iterate through each group
for (name, time_group), group_df in df_meter1.groupby(['name', '_time']):
    # initialize an empty dictionary for the group data
    group_dict = {"time": str(time_group)}

        # iterate through each row in the group
    for _, row in group_df.iterrows():
        # use column index 10:23 as the key and the value as the value
        for col in range(10, 24):  # 24 is exclusive, so it will loop till 23
            group_dict[df.columns[col]] = row[col]
    
    # append the group_dict to the data list in dict_field_meter1
    dict_field_meter1["data"].append(group_dict)

# print the resulting dictionary
print(dict_field_meter1)'''

'''import json
# Convert the dictionary to a JSON string with indentation
json_string = json.dumps(dict_field_meter1, indent=4)

# Write the formatted JSON string to a file
with open('output/dict_field_meter1-01.txt', 'w') as f:
    f.write(json_string)'''