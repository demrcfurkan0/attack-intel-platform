from pydantic import BaseModel, HttpUrl
from enum import Enum 
from datetime import datetime, timezone

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def serialize_pydantic_for_mongo(pydantic_model_instance: BaseModel) -> dict:
    data_dict = pydantic_model_instance.dict(exclude_none=True) 
    
    serialized_dict = {}
    for key, value in data_dict.items():
        if isinstance(value, HttpUrl):
            serialized_dict[key] = str(value)
        elif isinstance(value, Enum):
            serialized_dict[key] = value.value
        elif isinstance(value, datetime):
            serialized_dict[key] = value.isoformat()
        else:
            serialized_dict[key] = value
    return serialized_dict

def serialize_mongo_doc(doc: dict) -> dict:
    if "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc

# Load email credentials and settings 
def send_alert_email(subject: str, body: str):
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    recipient = os.getenv("EMAIL_RECIPIENT")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port_str = os.getenv("SMTP_PORT")

    if not all([sender, password, recipient, smtp_server, smtp_port_str]):
        print("Email settings are missing, mail could not be sent.")
        return

    try:
        smtp_port = int(smtp_port_str)
        # Create the email message.
        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = recipient
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        
        # Connect to the SMTP server and send the email.
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(message)
            print(f"Alert email sent to: {recipient}")

    except Exception as e:
        print(f"Error sending alert email: {e}")