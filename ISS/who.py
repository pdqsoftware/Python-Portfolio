import requests
import turtle


ASTRONAUT_URL = "http://api.open-notify.org/astros.json"
ISS_URL = "http://api.open-notify.org/iss-now.json"

#===============================================#
#============== FUNCTIONS ======================#
#===============================================#

def get_data_from_url(url_to_load):
    response = None
    try:
        response = requests.get(url_to_load)
    except:
        print("Some sort of connection error has occurred.")
        return None

    if response.status_code == 200:
        return response.json()
    else:
        return None


#===============================================#
#============== MAIN PROGRAM ===================#
#===============================================#

# Get the astronaut details from the URL and display them
astronaut_info = get_data_from_url(ASTRONAUT_URL)
if astronaut_info:
    print(f"There are {astronaut_info["number"]} astronauts currently in space:")
    astronauts = astronaut_info["people"]
    for astronaut in astronauts:
        print(f"{astronaut["name"]} is in the {astronaut["craft"]}")
else:
    print("The astronaut information is not currently available, please try again later!")

# Get ISS location and display it
location = get_data_from_url(ISS_URL)  #get_iss_location()

iss_longitude = float(location["iss_position"]["longitude"])
iss_latitude = float(location["iss_position"]["latitude"])
print(f"\nThe ISS is currently at:\n"
      f"Latitude: {iss_latitude} and\n"
      f"Longitude: {iss_longitude}")

# Test data - Cape Town:
# iss_latitude = -33.9221  # N to S
# iss_longitude = 18.423  # E to W

# Set up the screen
screen = turtle.Screen()
screen.setup(1075, 635)
screen.setworldcoordinates(-180, -90, 180, 90)

# Image courtesy of Wikipedia https://en.wikipedia.org/
screen.bgpic("./worlds_12000.gif")
screen.title("Location of the International Space Station")
screen.register_shape("./orion-5793_128.gif")

# Set up and display the ISS image
iss = turtle.Turtle()
# Image courtesy of Pixabay https://pixabay.com/
iss.shape("./orion-5793_128.gif")
iss.penup()
iss.goto(iss_longitude, iss_latitude)
# Test Data:  iss.goto(0 , 0)


screen.exitonclick()
