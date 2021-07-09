import requests
from twilio.rest import Client
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "*************************"
auth_token = "******************"
account_sid = "*****************************"
weather_params = {
    "lat": (write as your wish),
    "lon": (write as your wish),
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWN_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = (response.json())
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:

        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=" Rain Alert!!! Remember to bring an umbrella with you :-)",
        from_="(create an account on twillo and get your number)",
        to=(write a valid number as your wish)
    )
    print(message.status)

# print(weather_data["hourly"][0]["weather"][0]["id"])
