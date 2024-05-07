df2 = pd.read_csv("files/table_0.csv")
output_dict = {
  "name": df2['name'].iloc[0],
  "data": []
}
  
# Group DataFrame by "name" and "_time" and iterate through each group
for (name, time_group), group_df in df2.groupby(['name', '_time']):
    # Initialize an empty dictionary for the group data
    group_dict = {"time": str(time_group)}
  
    # Iterate through each row in the group
    for _, row in group_df.iterrows():
        # Use the field as the key and the value as the value
        group_dict[row['_field']] = row['_value']

    # Add the group data (including time and _values) to the output dictionary
    output_dict["data"].append(group_dict)
  
# Print the resulting dictionary
print(output_dict)