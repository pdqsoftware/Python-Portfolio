"""
This program demonstrates another 'funny' that occurs when a Python function is used in conjunction with
dynamic default arguments.
"""
import json


# Example 2.
# Two calls to the same function with different parameters
# They should each result in their own distinct dictionary - but they don't!
def process_json_data(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


print("The following calls to the same function should result in two distinct dictionaries:")
data1 = process_json_data('non-json data')
data1["one"] = 1
print(f"data1 = {data1}")

data2 = process_json_data('more non-json data')
data2["two"] = 2
print(f"data2 = {data2}")
