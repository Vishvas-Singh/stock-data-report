import smtplib
from email.mime.text import MIMEText
from credentials import EMAIL_USER, EMAIL_PASS, NOTIFICATION_EMAIL


def send_email(subject, message):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = NOTIFICATION_EMAIL

    smtp_server = 'smtp.gmail.com'
    smtp_port = 465 

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)