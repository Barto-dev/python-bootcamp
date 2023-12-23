import requests
from datetime import datetime


class SunriseSunsetAPI:
    ENDPOINT = "https://api.sunrise-sunset.org/json"

    def __init__(self, lat, lng):
        self.params = {"lat": lat, "lng": lng, "formatted": 0}

    def get_sunrise_sunset(self):
        response = requests.get(self.ENDPOINT, params=self.params)
        response.raise_for_status()
        data = response.json()
        sunrise = data["results"]["sunrise"]
        sunset = data["results"]["sunset"]
        formatted_sunrise = datetime.fromisoformat(sunrise)
        formatted_sunset = datetime.fromisoformat(sunset)
        return formatted_sunrise, formatted_sunset
