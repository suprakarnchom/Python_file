import pandas as pd
df = pd.read_csv('files/table_0.csv')
df.head()
#df_dict = df.to_dict(orient='records')
#print(df_dict[0])

df.columns
type(df)

import datetime

start_time = 1706500369
dt_object = datetime.datetime.fromtimestamp(timestamp)
start_time_iso = dt_object.isoformat()

print(start_time_iso)

# iso format = 2024-01-29 10:52:49
start_time_iso = '2024-01-29 10:52:49+00:00'

df['_time'] = pd.to_datetime(df['_time'])  # Ensure '_time' is in datetime format
mask = df['_time'] > start_time_iso  # Create a boolean mask
dt_filtered_df = df[mask]  # Apply the mask to the dfFrame

print(dt_filtered_df.head(1))

print(dt_filtered_df['_time'].min())
print(dt_filtered_df['_time'].max())

# Filter the dfFrame to only include the '_time' and '_field' columns
new_df = dt_filtered_df[['name','_time', '_field']]

new_df.head(2)

'''# Group by 'name' and '_time' and create a list of '_field' values for each group
grouped = new_df.groupby(['name', '_time'])['_field'].apply(list)

# Convert the result to a dictionary
final_dict = grouped.to_dict()

# Print the dictionary
print(final_dict)

import itertools

# Get the first n items of the dictionary
n = 5
top_items_dict = dict(itertools.islice(final_dict.items(), n))

# Print the top items
print(top_items_dict)'''

# Assuming df is your dfFrame
new_df = new_df.set_index(['name', '_time'])

df_dict = new_df.groupby(level=[0, 1]).apply(lambda x: x.to_dict(orient='records')).to_dict()

print(df_dict)

type(df_dict)

 # Delete the original 'df' variable
#del data

name = df_dict['name']
data = df_dict['_field']

#print first item in dictionary             
print(name)


# Get the first key in the dictionary
first_key = list(df_dict.keys())[0]

# Get the first item associated with the first key
first_item = df_dict[first_key][0]

# Print the first item
print(first_item)

# Convert the dfFrame to a dictionary
df_dict = new_df.groupby(level=[0, 1]).apply(lambda x: x.to_dict(orient='records')).to_dict()

# Create the final dictionary
final_dict = {
    'name': '',
    'data': [v[0] for v in df_dict[('meter 1',)].values()]
}

print(final_dict)

'''def create_dict(group):
    return {'time': group.name[1], **group.set_index('_field').to_dict()['value']}
grouped = new_df.groupby(['name', '_time']).apply(create_dict)
final_dict = {
    'name': 'meter 1',
    'df': grouped.tolist()
}

print(final_dict)'''
            

df_grouped = dt_filtered_df.groupby('_time')
print(df_grouped.head(1))

'''/device/meter/id => name
	Def device_meter_by_name(name,field=”all”,groupbytime=”15m”,from=”1706500369”,to=”now”,limit=1)'''

