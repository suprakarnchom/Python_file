'''df2 = df2.groupby("_time").first().reset_index()
df2.columns

import pandas as pd

df2 = df1[['name','_time','_field','_value']]
df2 = df2.groupby("_time").first().reset_index()
df2.columns

# from df2 turn it into a dictionary with the following structure
# {
    name: "meter 1",
    data: [
    {
        time: "2024-02-29T10:00:00.000Z",
        current_a: 28.56,
        current_b: 2.24,current_c: 26.24,
        current_t: 18.24,
        voltage_a: 223.56,
        voltage_b: 222.24,
        voltage_c: 223.24,
        kw_a: 4805.56,
        kw_b: 267.24,
        kw_c: 5016.24,
        kw_t: 3595.24,
        kwh_t: 2679675.24
    },
    {
        time: "2024-02-29T10:00:00.000Z",
        current_a: 28.56,
        current_b: 2.24,
        current_c: 26.24,
        current_t: 18.24,
        voltage_a: 223.56,
        voltage_b: 222.24,
        voltage_c: 223.24,
        kw_a: 4805.56,
        kw_b: 267.24,
        kw_c: 5016.24,
        kw_t: 3595.24,
        kwh_t: 2679675.24
    }
# which name is the first name in the name column
# and data is a list of dictionaries where each dictionary represents a row in the df2
# and the keys are the column names and the values are the values in the row
# the time is grouped by the time column and show every value in the column _filed as a key and the value in the column _value as the value

# Print the DataFrame
df2.head()

output_dict = {
    name: df2['name'],
    data: []
}


print(df2)'''
df2 = pd.read_csv("files/table_0.csv")
df2 = df2.groupby("_time").first().reset_index()
df2.columns
df2 = df2[['name','_time','_field','_value']]
df2.head(10)
df2._field.unique()
output_dict = {
  "name": df2['name'][0],
  "data": []
}

# Group DataFrame by "time" and iterate through each group
for time_group, group_df in df2.groupby("_time"):
    # Initialize an empty dictionary for the group data
    group_dict = {"time": str(time_group)}

    # Iterate through each row in the group
    for _, row in group_df.iterrows():
        # Use the field as the key and the value as the value
        group_dict[row['_field']] = row['_value']

        # Append another value from the same time group
        group_dict[row['_field']] = row['_value']
    
    # Add the group data (including time and _values) to the output dictionary
    output_dict["data"].append(group_dict)

# Print the resulting dictionary
print(output_dict)

print(df2['name'].unique())
group_data
group_dict

'''group_dict
del output_dict
del group_data
del time_group
del group_dict'''

with open('output04.txt', 'w') as f:
    f.write(str(output_dict))