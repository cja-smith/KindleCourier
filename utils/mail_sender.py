import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import os

class EmailServer:
    def __init__(self, sender_email, sender_password, kindle_email_address, smtp_host, smtp_port):
        self.sender_email=sender_email
        self.sender_password=sender_password
        self.kindle_email_address=kindle_email_address

        self.smtp_host=smtp_host
        self.smtp_port=smtp_port

    def send_email(self, filename='KindleCourier.epub'):

        date_today= datetime.today().strftime('%d-%m-%Y')
#        filename=f'KindleCourier {date_today}.epub'
        epub_path = os.path.join(os.getcwd(), 'attachments', filename)

        if not os.path.isdir(os.path.join(os.getcwd(), 'attachments')):
            raise NotADirectoryError(f'Unable to find attachments directory.')

        if not os.path.isfile(os.path.join(epub_path)):
            raise FileNotFoundError(f'Unable to find file "{filename}" in "{epub_path}".')

        #Create the email message
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = self.kindle_email_address
        msg['Subject'] = f'KindleCourier {date_today}'
        body = f'This is your automated news for today.'
        msg.attach(MIMEText(body, 'plain'))

        # Thank you python.readthedocs.io for having examples here 🙏
        # Attach the file
        try:
            with open(epub_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())

            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(part)
        except IOError as e:
            raise IOError(f'Error reading file "{epub_path}": {e}')
        # Send email over SMTP
        try:
            with smtplib.SMTP(self.smtp_host,self.smtp_port) as connection:
                connection.starttls()
                connection.login(self.sender_email,self.sender_password)
                connection.send_message(msg)
                return 'Message sent successfully!'

        except smtplib.SMTPResponseException as e:
            error_code = e.smtp_code
            error_message = e.smtp_error
            return (f'Failed to send email:\n'
                    f'Error code {error_code}\n'
                    f'Error message: {error_message}')
