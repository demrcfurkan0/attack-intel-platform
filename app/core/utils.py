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
        # Diğer tipler için basit atama, eğer iç içe Pydantic modelleri veya karmaşık tipler varsa
        # bu fonksiyonun daha kapsamlı olması gerekebilir.
        else:
            serialized_dict[key] = value
    return serialized_dict

def serialize_mongo_doc(doc: dict) -> dict:
    if "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc


def send_alert_email(subject: str, body: str):
    """Belirtilen konu ve içerikle bir uyarı e-postası gönderir."""
    
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    recipient = os.getenv("EMAIL_RECIPIENT")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port_str = os.getenv("SMTP_PORT")

    if not all([sender, password, recipient, smtp_server, smtp_port_str]):
        print("⚠️ E-posta ayarları .env dosyasında eksik, mail gönderilemedi.")
        return

    try:
        smtp_port = int(smtp_port_str)
        
        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = recipient
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(message)
            print(f"✅ Uyarı e-postası başarıyla gönderildi: {recipient}")

    except Exception as e:
        print(f"❌ E-posta gönderilirken hata oluştu: {e}")