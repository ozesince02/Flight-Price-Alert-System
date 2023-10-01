import smtplib

from twilio.rest import Client

TWILIO_SID = "AC5b20d4f0d259b2fbda40fb8d8d5e3032"
TWILIO_TOKEN = "68fbf1b262e7b4f6284f64a6b874dacf"
TWILIO_NUMBER = "+17432285531"
MY_NUMBER = "+919643090383"
MY_EMAIL = "testingpyproj13@gmail.com"
MY_PASSWORD = "testingP1#"


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
