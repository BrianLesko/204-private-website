import smtplib
from email.message import EmailMessage
from mysecrets import EMAIL, PASSWORD

class SimpleEmailSender:
    def __init__(self, subject, content, recipient_email):
        self.EMAIL = EMAIL
        self.PASSWORD = PASSWORD
        self.subject = subject
        self.content = content
        self.recipient_email = recipient_email

    def send_email(self):
        msg = EmailMessage()
        msg.set_content(self.content, subtype='html')
        msg['Subject'] = self.subject
        msg['To'] = self.recipient_email
        msg['From'] = EMAIL
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server: # use SSL for security
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)
