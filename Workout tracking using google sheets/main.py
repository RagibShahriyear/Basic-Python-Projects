import requests
from datetime import datetime

nutritionix_app_id = ID
nutritionix_api_key = KEY
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": nutritionix_app_id,
    "x-app-key": nutritionix_api_key,
    "x-remote-user-id": "0",
}

user_input = input("Tell me which exercises you did? ")

exercise_params = {
    "query": user_input,
    "gender": "male",
    "weight_kg": "60",
    "height_cm": "165",
    "age": "27",
}

exercise_response = requests.post(
    url=nutritionix_endpoint, headers=headers, json=exercise_params
)
result = exercise_response.json()

# TODO: Send data to sheety

sheety_get = (
    "https://api.sheety.co/7581521610f5574219f074473f7af673/myWorkouts/workouts"
)
sheety_post = (
    "https://api.sheety.co/7581521610f5574219f074473f7af673/myWorkouts/workouts"
)

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.today().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(url=sheety_post, json=sheet_inputs)
    print(sheet_response.json())
