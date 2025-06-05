"""
This program demonstrates some 'funnies' that occur when Python functions are used in conjunction with
dynamic default arguments.
"""
import json
import time
from datetime import datetime

# Example 1.
# Two calls to the same function with four seconds between them.
# They 'should' output different times - but they don't!
def log_record(message, log_time=datetime.now()):
    print(f"Message: {message} timed at {log_time}")

print("The following two console outputs should have different times associated with them.\n"
      "They should differ by 4 seconds - the time difference between two calls to the same function:")
time.sleep(4)
log_record("First log record")
print("Waiting 4 seconds...")
time.sleep(4)
log_record("Second log record")
########################################################################################

# Example 2.
# Two calls to the same function with different parameters
# They should produce different results - but they don't!
def process_json_data(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


# data1 = process_json_data('non-json data')
# data1["one"] = 1
# print(f"data1 = {data1}")
#
# data2 = process_json_data('more non-json data')
# data2["two"] = 2
# print(f"data2 = {data2}")