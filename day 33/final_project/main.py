import requests
from datetime import datetime
import smtplib

my_email = "email@email.com"
password = "password"

MY_LAT = 40.712776
MY_LNG = -74.005974

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def is_near():
    if 35 < iss_latitude < 45 and -70 > iss_longitude > -80:
        return True


def is_dark():
    if time_now.hour > 18 or time_now.hour < 7:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position
# and it is currently dark
if is_near() and is_dark():
    # Then email me to tell me to look up.
    # BONUS: run the code every 60 seconds.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            msg=f"Subject:ISS is near you\n\nHey, the ISS will be visible in the next few minutes",
            to_addrs="email@email"
        )
