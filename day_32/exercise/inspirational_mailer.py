import datetime as dt
import smtplib
from random import choice

FRIDAY = 4
quotes_list = []

MY_EMAIL = "example@gmail.com"
EMAIL_PASSWORD = "password"
GMAIL_SMTP = "smtp.gmail.com"

now = dt.datetime.now()

if now.weekday() == FRIDAY:
    with open("quotes.txt") as quotes:
        quotes_list = [quote.strip() for quote in quotes.readlines()]

    message = f"Subject:Inspirational Quote\n\n{choice(quotes_list)}"
    with smtplib.SMTP(GMAIL_SMTP) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message)
