import requests
from dotenv import load_dotenv
import os

load_dotenv()


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.spreadsheet_endpoint =  os.getenv("SHEETY_ENDPOINT")
        self.headers = {'Authorization': f'Basic {os.getenv('SHEETY_AUTH_KEY')}'}

    def get_all_data(self):
        response = requests.get(url=self.spreadsheet_endpoint)
        return response.json()
    
    def update_destination_code(self, data, row_id):
        body = {
            'price': {
                'iataCode': data
            }
        }
        response = requests.put(url=f'{self.spreadsheet_endpoint}/{row_id}', json=body, headers=self.headers)
        return response.text

        
        