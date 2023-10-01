import requests

SHEETY_ENDPOINT = "https://api.sheety.co/b1ec0e1cd7a08ffb359b95a0687ce8b4/flightDeals"


class DataManager:

    def __init__(self):
        self.customer_data = {}
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=f"{SHEETY_ENDPOINT}/prices")
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_email(self):
        customers_endpoint = f"{SHEETY_ENDPOINT}/users"
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
