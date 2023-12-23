from datetime import datetime, timezone
import smtplib
from sunrise_sunset_api import SunriseSunsetAPI
from iss_api import ISSAPI

# Barcelona
CITY_LAT = 41.390205
CITY_LNG = 2.154007

sunrise_sunset_api = SunriseSunsetAPI(CITY_LAT, CITY_LNG)
sunrise, sunset = sunrise_sunset_api.get_sunrise_sunset()

iss_api = ISSAPI()
iss_position = iss_api.fetch_iss_position()


def is_iss_overhead():
    if (
        CITY_LAT - 5 <= iss_position[0] <= CITY_LAT + 5
        and CITY_LNG - 5 <= iss_position[1] <= CITY_LNG + 5
    ):
        return True
    else:
        return False


def is_night():
    now = datetime.now()
    now_utc = now.astimezone(timezone.utc)
    if now_utc.hour >= sunset.hour or now_utc.hour <= sunrise.hour:
        return True
    else:
        return False


if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="your_email", password="your_password")
        connection.sendmail(
            from_addr="your_email",
            to_addrs="your_email",
            msg="Subject:Look Up\n\nThe ISS is above you in the sky.",
        )
