import requests
from twilio.rest import Client


OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
api_key = API_KEY
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

weather_param = {"appid": api_key, "lat": 23.780481, "lon": 90.361490}

will_rain = False

response = requests.get(OWM_ENDPOINT, params=weather_param)
response.raise_for_status()
condition_code = response.json()["weather"][0]["id"]
if condition_code < 1000:
    will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella. ☂️",
        from_="+12177330537",
        to=TO,
    )
    print(message.status)
