import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DataManager:
    def __init__(self):
        """
        Initialize the DataManager class with environment variables and set up headers for API requests.
        """
        self._sheety_username = os.getenv("SHEETY_USERNAME")
        self._sheety_password = os.getenv("SHEETY_PASSWORD")
        self._prices_endpoint = os.getenv("SHEETY_PRICES_ENDPOINT")
        self._users_endpoint = os.getenv("SHEETY_USERS_ENDPOINT")
        self._auth_header = {
            "Authorization": "Basic YW5pc3J1c3phbm5hOndpbnRlckAxMjM0NQ=="
        }

        self.destination_data = {}

    def get_destination_data(self):
        """
        Retrieve destination data from the prices Google Sheet.

        Returns:
            list: A list of dictionaries containing destination data.
        """
        response = requests.get(
            url=self._prices_endpoint,
            headers=self._auth_header
        )
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """
        Update the IATA codes in the prices Google Sheet.
        """
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self._prices_endpoint}/{city['id']}",
                json=new_data,
                headers=self._auth_header
            )
            print(response.text)

    def get_customer_emails(self):
        """
        Retrieve customer emails from the users Google Sheet.

        Returns:
            list: A list of dictionaries containing user data.
        """
        response = requests.get(
            url=self._users_endpoint,
            headers=self._auth_header
        )
        response.raise_for_status()
        data = response.json()
        return data["users"]
