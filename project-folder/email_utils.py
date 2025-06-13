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

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, NOTIFICATION_EMAIL, msg.as_string())