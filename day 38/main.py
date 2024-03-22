import requests
from datetime import datetime

NUTRITIONIX_APP_ID = "app_id"
NUTRITIONIX_API_KEY = "api_key"
NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "male"
WEIGHT_KG = "86"
HEIGHT_CM = "176"
AGE = "21"

SHEETY_URL = "https://api.sheety.co/a4d2c9686e7338e3f7b61aa9e79b6dc4/copyOfMyWorkouts/workouts"

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

params = {
    "query": "i ran 3km in 30 minutes",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(NUTRITIONIX_URL, json=params, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        SHEETY_URL,
        json=sheet_inputs,
        auth=(
            "admin",
            "12345678",
        )
    )

    print(sheet_response.text)