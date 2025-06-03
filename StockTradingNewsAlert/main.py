from datetime import timedelta
import requests
import datetime
import smtplib
from email.message import EmailMessage


# Stocks #
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_NEWS_PERCENT_CHANGE = 5
STOCK_API_KEY = "6ZT2DFL101EKIGP1"
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

# Email #
SOURCE_EMAIL_ADDRESS = "pdqsoftware.aws@gmail.com"
# Use the App Password created on Day 32
MY_EMAIL_PASSWORD = "wlikuzooyjflizro"
DESTINATION_EMAIL_ADDRESS = "pdqsoftware@gmail.com"


live_mode = False  # Limited to 25 API calls per day

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

def get_news():
    news_parameters = {
        "apikey": NEWS_API_KEY,
        "q": NEWS_SEARCH_TEXT,
        # "from": "2025-04-21",
        # "to": "2025-04-22",
        "sortBy": "publishedAt",
        "searchin": "title",
        "language": "en",
    }

    news_response = requests.get(url=NEWS_URL, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()

    # Get MAX_NEWS_ITEMS news items
    # news_list = []
    # count = 0
    # print(f"articles: {news_data["articles"]}")
    print(f"first three: {news_data["articles"][:3]}")
    # for item in news_data["articles"]:
    #     news_list.append(item)
    #     count += 1
    #     if count >= MAX_NEWS_ITEMS:
    #         break

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
    print(email_message)

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

if live_mode:
    stock_data = get_stock_details()
    print(stock_data)

    # meta_data = stock_data["Meta Data"]
    #
    # time_data = stock_data["Time Series (60min)"]
    # print(time_data)
    # print(time_data["2025-04-16 19:00:00"])
    # print(meta_data)

    now = datetime.datetime.now()
    print(now)
    day_minus_one = f"{now.date() - timedelta(5)} {LOOKUP_TIME}"   # 1
    print(f"day_minus_one: {day_minus_one}")
    day_minus_two = f"{now.date() - timedelta(6)} {LOOKUP_TIME}"   # 2
    print(f"day_minus_two: {day_minus_two}")
    time_data_one = stock_data["Time Series (60min)"][day_minus_one]["4. close"]
    print(time_data_one)
    time_data_two = stock_data["Time Series (60min)"][day_minus_two]["4. close"]
    print(time_data_two)

    difference = abs(float(time_data_one) - float(time_data_two))
    print(f"Difference: {round(difference, 2)}")
    print(f"% difference: {round(abs( (float(time_data_two) - float(time_data_one)) / float(time_data_two) * 100), 2)}")

else:
    ### NOTE:
    ### The following lines are examples only - DOWN 12.87 points
    time_data_one = 242.2500
    time_data_two = 255.1200  # 250.3500
    difference = abs(time_data_two - time_data_one)
    print(difference)

difference_percent = difference / float(time_data_two) * 100
difference_sign = 1 if float(time_data_two) - float(time_data_one) < 0 else -1

if difference_percent > STOCK_NEWS_PERCENT_CHANGE:
    print("Get news!")
    news_summary = get_news()
    record_count = min(MAX_NEWS_ITEMS, len(news_summary))

    if record_count > 0:
        for i in range(0, record_count):
            message_to_send = format_news_message(difference_percent * difference_sign, news_summary[i])
            # print(message_to_send)
            send_news_email(message_to_send)
