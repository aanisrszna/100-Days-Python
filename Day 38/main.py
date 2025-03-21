import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()


# Nutritionix API credentials (replace with your actual credentials)
GENDER = "female"
AGE = 23
WEIGHT_KG = 57.8
HEIGHT_CM = 162


# Nutritionix exercise endpoint
EXERCISE_API_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_query = input("Describe your exercise: ")
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

payload = {
    "query": exercise_query ,
    "gender": GENDER,  # Adjust based on the user
    "weight_kg": WEIGHT_KG,  # Adjust weight (in kilograms)
    "height_cm": HEIGHT_CM,  # Adjust height (in centimeters)
    "age": AGE  # Adjust age (in years)
}

response = requests.post(EXERCISE_API_URL, json=payload, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs={
        "workout":{
            "date":today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type":"application/json",
    }
    sheet_response =requests.post(SHEET_ENDPOINT, json=sheet_inputs, headers= sheet_headers)
    print(sheet_response.text)

