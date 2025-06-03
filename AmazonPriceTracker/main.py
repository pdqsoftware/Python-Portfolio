import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Private Email Info. #
source_email = os.getenv("SOURCE_EMAIL_ADDRESS")
email_password = os.getenv("MY_EMAIL_PASSWORD")
destination_email = os.getenv("DESTINATION_EMAIL_ADDRESS")

URL = "https://www.amazon.com/dp/B075CYMYK6?th=1"
PRODUCT_NAME = "Instant Pot"
PRICE_CUTOFF = 100

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en-GB;q=0.9,en;q=0.8",
}

#===============================================#
#============== FUNCTIONS ======================#
#===============================================#

def send_email(email_message):
    msg = EmailMessage()
    msg.set_content(email_message)
    msg["Subject"] = "Amazon Price Tracker"
    msg["From"] = source_email
    msg["To"] = destination_email

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=source_email, password=email_password)
        connection.send_message(msg)
        connection.quit()

def format_email_contents(name, detail, price):
    email_message = f"Your product: '{name}'\nDescription: {detail}\n"
    email_message += f"Has gone below ${PRICE_CUTOFF}.\n"
    email_message += f"It is now priced at ${price}.  Buy, buy, buy...\n"
    return email_message

#===============================================#
#============== MAIN PROGRAM ===================#
#===============================================#

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# Get the price
price_tag = soup.select_one(selector=".a-price .a-offscreen")
# Convert it to a floating point number
price = float(price_tag.getText().split("$")[1])

# Get the product detail
product_detail = soup.select_one(selector="#productTitle").getText().strip()

product_name = product_detail.split(",")[0].strip()
full_product_description = product_detail.split(",", 1)[1].strip()

if price < PRICE_CUTOFF:
    # Prepare and send email
    message = format_email_contents(product_name, full_product_description, price)
    send_email(message)
