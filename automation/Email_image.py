import email, smtplib, ssl
import os
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
from dotenv import load_dotenv


load_dotenv()


def custom_sort(elem):
    number = re.findall(r"[0-9]+", elem)
    return int(number[0])


class EmailSettings(MIMEMultipart):
    def __init__(self):
        super().__init__()
        self.email_information = {
            "subject": "Picture Time",
            "body": "Here's another one because why not.",
            "sender_email": os.environ.get("sender_email"),
            "receiver_email": os.environ.get("reciever_email"),
            "password": os.environ.get("password"),
        }
        self.message = MIMEMultipart()
        self.message["From"] = self.email_information["sender_email"]
        self.message["To"] = self.email_information["receiver_email"]
        self.message["Subject"] = self.email_information["subject"]
        self.message["Bcc"] = self.email_information["receiver_email"]
        self.files = [f for f in os.listdir(f"created_images")]

    def __str__(self):
        return f"{self.email_information}"

    def send_email(self):
        self.message.attach(MIMEText(self.email_information["body"], "plain"))
        self.files.sort(key=custom_sort)
        filename = self.files[-1]
        self.files.sort(key=custom_sort)

        with open(f"created_images/{filename}", "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        self.message.attach(part)
        text = self.message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(
                    self.email_information["sender_email"],
                    self.email_information["password"],
                )
                server.sendmail(
                    self.email_information["sender_email"],
                    self.email_information["receiver_email"],
                    text,
                )
        except ConnectionError as e:
            print(f"Failed due to {e}")
        finally:
            print(f"Sent")
