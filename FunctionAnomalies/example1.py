"""
This program demonstrates a 'funny' that occurs when a Python function is used in conjunction with
dynamic default arguments.
"""

import time
from datetime import datetime


# Example 1.
# Two calls to the same function with four seconds between them.
# They 'should' output different times - but they don't!
def log_record(message, log_time=datetime.now()):
    print(f"Message: {message} timed at {log_time}")

print("The following two console outputs should have different times associated with them.\n"
      "They should differ by 4 seconds - the time difference between two calls to the same function:")
log_record("First log record")
print("Waiting 4 seconds...")
time.sleep(4)
log_record("Second log record")
