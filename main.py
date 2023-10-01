import datetime
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

notification_manager = NotificationManager()
flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)
ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
six_months_from_today = datetime.datetime.now() + datetime.timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:

        users = data_manager.get_customer_email()
        email = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}." \
               f"{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        message = f"Low price alert! Only 💶 {flight.price} to fly from {flight.origin_city}-{flight.origin_airport}" \
                  f"to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop overs, via {flight.via_city}."

            if flight.stop_overs > 1:
                message += f"and via {flight.via_city_2} on return flight."

            notification_manager.send_email(message=message, email=email, link=link)


