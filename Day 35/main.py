import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "API KEY"
account_sid = "ACCOUNT SID"
auth_token ="AUTH TOKEN"

weather_params = {
    "lat": 3.202990,
    "lon": 101.732269,
    "appid": api_key
}

# Make the API request
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()  # Raise an exception for HTTP errors

# Parse the JSON response
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int (condition_code)<700:
        will_rain = True
if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔.",
        from_="+13343669921",
        to="+60174757964",
    )

    print(message.status)
