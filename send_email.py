import os
import smtplib
import ssl
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()
password = os.getenv("PASSWORD_GMAIL")


def send_mail(name, email, phone):
    context = ssl.create_default_context()
    text = f"""
        ФИО: {name}
        Электронная почта: {email}
        Контакный номер: {phone}"""
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['Subject'] = 'Заявка от чат-бота в телеграм'

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login("vildanzufarovic@gmail.com", password=password)
        server.sendmail("vildanzufarovic@gmail.com", "di.altynbaeva@gmail.com", msg.as_string())
        print("Сообщение успешно отправлено")
