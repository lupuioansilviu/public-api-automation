import requests
from typing import Optional


class AgifyClient:
    BASE_URL = "https://api.agify.io"

    def predict_age(self, name: str, country_id: Optional[str] = None):
        params = {"name": name}
        if country_id:
            params["country_id"] = country_id
        return requests.get(self.BASE_URL, params=params, timeout=15)
