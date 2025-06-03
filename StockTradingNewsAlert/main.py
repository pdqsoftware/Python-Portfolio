from datetime import timedelta
import requests
import datetime
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Stocks #
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_NEWS_PERCENT_CHANGE = 5
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
STOCK_URL = "https://www.alphavantage.co/query"
FUNCTION = "TIME_SERIES_INTRADAY"  # TIME_SERIES_DAILY
LOOKUP_TIME = "19:00:00"

# News #
NEWS_API_KEY = "7173c1e27635495db41d4f3669337408"
NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_SEARCH_TEXT = "tesla"
# NEWS_SEARCH_TEXT = "manchester united"
# NEWS_SEARCH_TEXT = "Ruben Amorim"
MAX_NEWS_ITEMS = 3

# Private Email Info. #
SOURCE_EMAIL_ADDRESS = os.getenv("SOURCE_EMAIL_ADDRESS")
MY_EMAIL_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")
DESTINATION_EMAIL_ADDRESS = os.getenv("DESTINATION_EMAIL_ADDRESS")


live_mode = False  # Live mode limited to 25 API calls per day

#===============================================#
#============== FUNCTIONS ======================#
#===============================================#

def get_news():
    news_parameters = {
        "apikey": NEWS_API_KEY,
        "q": NEWS_SEARCH_TEXT,
        "sortBy": "publishedAt",
        "searchin": "title",
        "language": "en",
    }

    news_response = requests.get(url=NEWS_URL, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()

    # Get MAX_NEWS_ITEMS news items
    return news_data["articles"][:MAX_NEWS_ITEMS]  # news_list

def format_news_message(percent_change, news_item):
    percent_change = round(percent_change, 2)
    updown_icon = "🔻"
    if percent_change > 0:
        updown_icon = "🔺"

    percent_change = abs(percent_change)

    message = f"{NEWS_SEARCH_TEXT}:  {updown_icon} {percent_change}%\n"
    message += f"Headline:\n{news_item["title"]}\n"
    message += f"Brief:\n{news_item["description"]}\n\n\n"
    return message

def send_news_email(email_message):
    # print(email_message)

    msg = EmailMessage()
    msg.set_content(email_message)
    msg["Subject"] = "Alpha Vantage Stock News"
    msg["From"] = SOURCE_EMAIL_ADDRESS
    msg["To"] = DESTINATION_EMAIL_ADDRESS

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SOURCE_EMAIL_ADDRESS, password=MY_EMAIL_PASSWORD)
        connection.send_message(msg)
        connection.quit()

def get_stock_details():

    stock_parameters = {
        "apikey": STOCK_API_KEY,
        "interval": "60min",
        "symbol": STOCK,
        "function": FUNCTION,
    }

    stock_response = requests.get(url=STOCK_URL, params=stock_parameters)
    stock_response.raise_for_status()

    return stock_response.json()

#===============================================#
#============== MAIN PROGRAM ===================#
#===============================================#

if live_mode:
    stock_data = get_stock_details()
    # print(stock_data)

    now = datetime.datetime.now()
    day_minus_one = f"{now.date() - timedelta(5)} {LOOKUP_TIME}"   # 1
    day_minus_two = f"{now.date() - timedelta(6)} {LOOKUP_TIME}"   # 2
    time_data_one = stock_data["Time Series (60min)"][day_minus_one]["4. close"]
    time_data_two = stock_data["Time Series (60min)"][day_minus_two]["4. close"]

    difference = abs(float(time_data_one) - float(time_data_two))

else:
    ### NOTE:
    ### The following lines are examples only - DOWN 12.87 points
    time_data_one = 242.2500
    time_data_two = 255.1200
    difference = abs(time_data_two - time_data_one)

difference_percent = difference / float(time_data_two) * 100
difference_sign = 1 if float(time_data_two) - float(time_data_one) < 0 else -1

if difference_percent > STOCK_NEWS_PERCENT_CHANGE:
    # print("Get news!")
    news_summary = get_news()
    record_count = min(MAX_NEWS_ITEMS, len(news_summary))

    if record_count > 0:
        for i in range(0, record_count):
            message_to_send = format_news_message(difference_percent * difference_sign, news_summary[i])
            # print(message_to_send)
            send_news_email(message_to_send)
