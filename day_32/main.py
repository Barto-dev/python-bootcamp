import datetime as dt
import pandas
import smtplib
from random import randint

MY_EMAIL = "example@gmail.com"
EMAIL_PASSWORD = "password"
GMAIL_SMTP = "smtp.gmail.com"

data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")

now = dt.datetime.now()

for birthday in birthdays:
    if now.month == birthday["month"] and now.day == birthday["day"]:
        with open(f"letter_templates/letter_{randint(1, 3)}.txt") as letter:
            message = letter.read().replace("[NAME]", birthday["name"])

        with smtplib.SMTP(GMAIL_SMTP) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday["email"],
                msg=f"Subject:Happy Birthday\n\n{message}",
            )
