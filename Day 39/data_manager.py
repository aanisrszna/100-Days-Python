import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/01d066a2740ceb1c956e7b16cf36fbcc/flightDeals/prices"


class DataManager:

    def __init__(self):
        # Set up the Authorization header directly
        self._auth_header = {
            "Authorization": "Basic YW5pc3J1c3phbm5hOndpbnRlckAxMjM0NQ=="
        }
        self.destination_data = {}

    def get_destination_data(self):
        # GET request to retrieve data from Google Sheet
        response = requests.get(
            url=SHEETY_PRICES_ENDPOINT,
            headers=self._auth_header  # Include Authorization header
        )
        response.raise_for_status()  # Raise an error for HTTP issues
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            # PUT request to update data in Google Sheet
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self._auth_header  # Include Authorization header
            )
            if response.status_code == 403:
                print(f"Permission denied for updating row {city['id']}. Check Sheety permissions.")
            else:
                response.raise_for_status()
                print(f"Updated row {city['id']} with IATA code {city['iataCode']}.")
