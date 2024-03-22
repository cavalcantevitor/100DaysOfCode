import smtplib
import datetime as dt
import random

my_email = "teste.vitoralves2c@gmail.com"
password = "qrrl dmur dgwq cphh "

now = dt.datetime.now()
day_of_the_week = now.weekday()

if day_of_the_week == 4:
    with open("quotes.txt", "r") as file:
        data = file.readlines()
        new_data = [string.replace("\n", "") for string in data]

    random_quote = random.choice(new_data)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            msg=f"Subject:Motivational Quote\n\n{random_quote}",
            to_addrs="vitoralves2c@gmail.com"
        )

    print("Email was sent")