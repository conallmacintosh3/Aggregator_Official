import smtplib
from email.message import EmailMessage


def email():
    message = EmailMessage()
    message['Subject'] = "**DAILY NEWS**"
    message['From'] = "email"
    message['To'] = "email"
    message.set_content(
        open('article_storage.txt', 'r').read()
    )

    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login("email",
               "password")
    smtp.send_message(message)
    smtp.quit()