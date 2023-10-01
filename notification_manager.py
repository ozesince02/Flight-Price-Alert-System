import smtplib

from twilio.rest import Client

TWILIO_SID = "YOUR TWILIO SID"
TWILIO_TOKEN = "YOUR TWILIO TOKEN"
TWILIO_NUMBER = "YOUR TWILIO NUMBER"
MY_NUMBER = "YOU PHONE NUMBER"
MY_EMAIL = "YOUR EMAIL ID"
MY_PASSWORD = "YOU PASSWORD"


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
        )
        print(message.sid)

    def send_email(self, message, email, link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, "ioveumau23#")
            for mail in email:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=mail,
                    msg=f"Subject: Low Price Alert!\n\n{message}\n{link}".encode('utf-8')
                )
