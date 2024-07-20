from dotenv import load_dotenv
import os
import requests

load_dotenv()

class FlightSearch:
    def __init__(self) -> None:
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_SECRET_KEY")
        self._token = self.get_new_token()


    def get_destination_code(self, city_name):
        endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        payload = {
            "keyword" : city_name,

            }
        header = {
            "Authorization" : f'Bearer {self._token}'
            }
        response = requests.get(url=endpoint, params=payload, headers=header)
        data = response.json()
        return data.get('data')[0]['iataCode']

    def get_new_token(self):
        token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {"Content-Type" : "application/x-www-form-urlencoded"}
        payload = {
            'grant_type': 'client_credentials',
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response = requests.post(url=token_endpoint, data=payload, headers=headers )
        print(response.text)
        return response.json()['access_token']
        
    #This class is responsible for talking to the Flight Search API.
    