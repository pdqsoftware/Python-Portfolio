import requests
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# TODO: Replace the commenting of steps with a user action input

# Example from the Pixela webpage
# $ curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes", "thanksCode":"ThisIsThanksCode"}'
# {"message":"Success. Let's visit https://pixe.la/@a-know , it is your profile page!","isSuccess":true}


PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = "graph1"

print(USERNAME)
print(TOKEN)

#===============================================#
#============== MAIN PROGRAM ===================#
#===============================================#

walking_date = input("Enter your exercise date (YYYYMMDD): ")
walking_distance = input("Enter your exercise distance for this day in KM: ")

user_params = {
    "token": TOKEN,  # Self-generated unique token
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

'''
Comment out all of the five steps below. 
Then uncomment them one at a time in order to perform each task, as required.
'''

### Step 1.
# # Create user account
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(f"Step 1: {response.text}")
##################################################################################

### Step 2.
# # Create a graph definition
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(f"Step 2: {response.text}")
##################################################################################

### Step 3.
# Post value to the graph
post_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": walking_date,
    "quantity": walking_distance,
}

response = requests.post(url=post_endpoint, json=pixel_data, headers=headers)
print(f"Step 3: {response.text}")
##################################################################################

### Step 4.
# Amend a pixel
update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{walking_date}"

pixel_data = {
    "quantity": walking_distance,
}

# response = requests.put(url=update_endpoint, json=pixel_data, headers=headers)
# print(f"Step 4: {response.text}")
##################################################################################

### Step 5.
# Delete a pixel
delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{walking_date}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(f"Step 5: {response.text}")
##################################################################################