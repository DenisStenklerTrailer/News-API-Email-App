import smtplib
import ssl
import os

host = "smtp.gmail.com"
port = 465

username = "olga.trojer@gmail.com"
password = "mvcyzomecnqupgri"

reciever = "denis.stenkler@gmail.com"
context = ssl.create_default_context()

def send_email(message):
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username,password)
        server.sendmail(username, reciever, message)
