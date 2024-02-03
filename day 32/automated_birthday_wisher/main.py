import datetime as dt
import pandas as pd
import random
import smtplib

EMAIL = ""
PASSWORD = ""

now = dt.datetime.now()
month = now.month
day = now.day

birthdays = pd.read_csv("birthdays.csv")

for index, row in birthdays.iterrows():
    if row["month"] == 2 and row["day"] == 2:

        random_number = random.randint(1, 3)
        with open(f"letter_templates/letter_{random_number}.txt", "r") as file:
            letter = file.read()
            new_letter = letter.replace("[NAME]", f"{row["name"]}")

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                msg=f"Subject:Happy birthday\n\n{new_letter}",
                to_addrs=f"{row["email"]}"
            )