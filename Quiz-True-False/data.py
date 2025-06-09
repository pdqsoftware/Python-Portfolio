import requests


"""
This module loads the questions from the 'Open Trivia Database' when the program starts.
It stores them into the questions list ready for use by the other parts of the application.
"""

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
questions = data["results"]

question_data = questions
