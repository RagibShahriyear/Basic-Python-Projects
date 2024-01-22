import requests
import datetime as dt
import smtplib
import time

MY_EMAIL = "69pythontester420@gmail.com"
MY_PASS = "@68^IUICz3r*p5Det!"

MY_LAT = 23.810331
MY_LNG = 90.412521


def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    iss_longitude = float(response.json()["iss_position"]["longitude"])
    iss_latitude = float(response.json()["iss_position"]["latitude"])

    # Your position is within +5 or +5 degrees of the ISS position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <=iss_longitude <= MY_LNG+5:
        return True


def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sunrise = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        )