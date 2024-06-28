import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 33.502491  # Your latitude
MY_LONG = 73.106991  # Your longitude
MY_PASSWORD = 'vgrumgyfhuwjooov'
MY_EMAIL = 'joemom7860@gmail.com'
TO_EMAIL = 'omg.its.muhid@gmail.com'


def iss_is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (iss_latitude - 5 <= MY_LAT <= iss_latitude + 5) and (iss_longitude - 5 <= MY_LONG <= iss_longitude + 5)

# Your position is within +5 or -5 degrees of the ISS position.


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour

    return sunset <= current_hour or current_hour <= sunrise


while True:
    time.sleep(60)
    if is_dark() and iss_is_close():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg='Subject: ISS is close \n\nLook up and find the satellite'
            )
