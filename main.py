import os
import time

from dotenv import load_dotenv

from guardian_client import GuardianAPIClient
from models import Article
from utils.mail_sender import EmailServer

load_dotenv()

GUARDIAN_API_KEY = os.getenv('GUARDIAN_API_KEY')
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
KINDLE_EMAIL = os.getenv('KINDLE_EMAIL')
SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PORT = os.getenv('SMTP_PORT')

api_client = GuardianAPIClient(api_key=GUARDIAN_API_KEY)
server = EmailServer(sender_email=EMAIL_ADDRESS,
                     sender_password=EMAIL_PASSWORD,
                     kindle_email_address=KINDLE_EMAIL,
                     smtp_host=SMTP_HOST,
                     smtp_port=SMTP_PORT)

urls = api_client.get_top_story_urls()

for url in urls:
    article_data = api_client.generate_article(url)

    if not article_data.get('ignore'):
        article = Article(
            headline=article_data['headline'],
            trailText=article_data['trailText'],
            byline=article_data['byline'],
            body=article_data['body'],
            thumbnail=article_data['thumbnail'],
        )
    time.sleep(1)


'''
Convert articles into ePub
'''

server.send_email()