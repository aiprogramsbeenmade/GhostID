import requests
import time

class OSMClient:
    def __init__(self):
        self.base_url = "https://nominatim.openstreetmap.org/search"
        self.headers = {
            "User-Agent": "GhostID_Framework_Educational_Bot"
        }

    def fetch_real_address(self, city="Roma"):
        params = {
            "city": city,
            "format": "json",
            "addressdetails": 1,
            "limit": 1
        }
        try:
            response = requests.get(self.base_url, params=params, headers=self.headers)
            if response.status_code == 200 and response.json():
                address_data = response.json()[0].get("address", {})

                # Estraiamo solo i componenti essenziali per un look pulito
                road = address_data.get("road", "Via Centrale")
                suburb = address_data.get("suburb", "")
                city_name = address_data.get("city") or address_data.get("town") or address_data.get("village")
                postcode = address_data.get("postcode", "")

                clean_address = f"{road}, {suburb + ', ' if suburb else ''}{city_name}, {postcode}, Italia"
                return {"display_name": clean_address}
        except Exception as e:
            return None