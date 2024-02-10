import requests
from twilio.rest import Client

api_key = ""
auth_token = ""
account_sid = ""

weather_params = {
    "lat": 1,
    "lon": 1,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
weather_data = response.json()

data = [_["weather"][0]["id"] for _ in weather_data["list"]]

will_rain = False
for weather_id in data:
    if weather_id < 700:
        will_rain = True
if will_rain:
    account_sid = account_sid
    auth_token = auth_token
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='',
        to='',
        body="It will rain! Remember to bring an umbrella!"
    )

    print(message.status)