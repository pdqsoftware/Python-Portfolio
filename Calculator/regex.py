import re

pattern = r"^[+\-*/]$"

input_string = "/"

print(bool(re.match(pattern, input_string)))