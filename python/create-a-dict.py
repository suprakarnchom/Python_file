import pandas as pd

# Create a sample DataFrame
data = {
  "time": pd.to_datetime(["2024-02-29T10:00:00.000Z", "2024-02-29T10:00:00.000Z", "2024-02-29T10:00:00.000Z"]),
  "current_a": [28.56, 28.56, 28.56],
  "current_b": [2.24, 2.24, 2.24],
  # ... include all your data columns here
  "kwh_t": [2679675.24, 2679675.24, 2679675.24]
}

df = pd.DataFrame(data)
df.head()

# Define the dictionary structure
meter_data = {
  "name": "meter 1",
  "data": []
}

# Convert each row of DataFrame to a dictionary and add it to the list
for index, row in df.iterrows():
  data_point = {
    "time": row["time"].strftime('%Y-%m-%dT%H:%M:%S.%fZ'),  # Format timestamp as needed
    "current_a": row["current_a"],
    "current_b": row["current_b"],
    # ... include all data points as key-value pairs
    "kwh_t": row["kwh_t"]
  }
  meter_data["data"].append(data_point)

print(meter_data)