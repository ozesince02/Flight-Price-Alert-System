# Flight Price Tracker and Notification System

## Overview

This project is a Flight Price Tracker and Notification System that allows users to track flight prices from a specified origin city (LON, London, by default) to various destinations. The system periodically checks for low-priced flights and sends notifications to registered users via SMS (using Twilio) and email (using Gmail's SMTP server). It utilizes external APIs to fetch flight and destination data.

## Files

The project consists of several Python files:

1. **main.py**: The main script that orchestrates the flight price tracking and notification process.

2. **data_manager.py**: Manages customer and destination data using the Sheety API.

3. **flight_data.py**: Defines the `FlightData` class for storing flight details.

4. **flight_search.py**: Interfaces with the Tequila Kiwi flight search API to fetch flight information.

5. **notification_manager.py**: Handles the sending of SMS and email notifications using Twilio and Gmail.

## Usage

To use this Flight Price Tracker and Notification System:

1. Set up your Twilio account and obtain your SID and TOKEN. Replace `TWILIO_SID` and `TWILIO_TOKEN` in `notification_manager.py` with your credentials.

2. Configure your Twilio phone number (`TWILIO_NUMBER`) and recipient's number (`MY_NUMBER`).

3. Set up your Gmail account for sending emails. Replace `MY_EMAIL` and `MY_PASSWORD` in `notification_manager.py` with your Gmail credentials. Ensure that you allow less secure apps in your Gmail account settings or use an app password.

4. Run `main.py` to start the flight price tracking process. The script will periodically check for low-priced flights and send notifications to registered users.

## Dependencies

This project relies on the following external libraries and APIs:

- Twilio: For sending SMS notifications.
- Gmail SMTP: For sending email notifications.
- Sheety API: For managing customer and destination data.
- Tequila Kiwi API: For retrieving flight and destination information.

Please ensure that you have installed the required Python packages using `pip install -r requirements.txt` before running the project.

## Customization

You can customize various aspects of this project, including the origin city, notification criteria, and the frequency of flight price checks. Modify the code in `main.py` and other relevant files to tailor the system to your specific requirements.

## Author

Pulkit Choudhary

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Twilio](https://www.twilio.com/) for SMS notifications.
- [Tequila Kiwi](https://developers.kiwi.com/) for flight data.
- [Sheety](https://sheety.co/) for managing data.

