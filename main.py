import os
from datetime import datetime
import requests

exercise_text = input("Tell me which exercises you did: ")

APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')
GENDER = os.getenv("GENDER")
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")

EXERCISE_END_POINT = os.getenv("EXERCISE_END_POINT")

sheet_headers = {
    "Authorization": os.getenv('BEARER_TOKEN')
}

APP_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

post_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

SHEET_END_POINT = os.getenv("SHEET_END_POINT")

response = requests.post(EXERCISE_END_POINT, headers=APP_headers, json=post_parameters)
result = response.json()['exercises'][0]
sheet_posted = {
    "workout": {
        "date": today_date,
        "time": today_time,
        "exercise": result['name'].title(),
        "duration": result['duration_min'],
        "calories": result['nf_calories']
    }
}
Sheet_post = requests.post(url=SHEET_END_POINT, json=sheet_posted, headers=sheet_headers)
print(Sheet_post.json())
