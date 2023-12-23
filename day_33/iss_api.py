import requests


class ISSAPI:
    ENDPOINT = "http://api.open-notify.org/iss-now.json"

    def fetch_iss_position(self):
        response = requests.get(self.ENDPOINT)
        response.raise_for_status()
        data = response.json()
        iss_position = (
            float(data["iss_position"]["latitude"]),
            float(data["iss_position"]["longitude"]),
        )
        return iss_position
