import datetime

# create function to convert timestamp to iso format
def convert_timestamp_to_iso(timestamp):
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    iso_format = dt_object.isoformat()
    return iso_format

# test the function
convert_timestamp_to_iso(1706500369)

# create functio to convert iso format to timestamp
def convert_iso_to_timestamp(iso_format):
    dt_object = datetime.datetime.fromisoformat(iso_format)
    timestamp = dt_object.timestamp()
    return timestamp

# test the function
convert_iso_to_timestamp('2024-03-31T00:00:00')