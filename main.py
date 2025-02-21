import os
import time

from dotenv import load_dotenv
from datetime import datetime

from guardian_client import GuardianAPIClient
from models import Article
from utils.ebook_generator import EBookGenerator
from utils.mail_sender import EmailServer

load_dotenv()

GUARDIAN_API_KEY = os.getenv('GUARDIAN_API_KEY')
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
KINDLE_EMAIL = os.getenv('KINDLE_EMAIL')
SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PORT = os.getenv('SMTP_PORT')

def main():
    api_client = GuardianAPIClient(api_key=GUARDIAN_API_KEY)
    server = EmailServer(sender_email=EMAIL_ADDRESS,
                         sender_password=EMAIL_PASSWORD,
                         kindle_email_address=KINDLE_EMAIL,
                         smtp_host=SMTP_HOST,
                         smtp_port=SMTP_PORT)

    date_today = datetime.today().strftime('%d-%m-%Y')
    filename=f'KindleCourier {date_today}.epub'

    urls = api_client.get_top_story_urls()
    articles = []
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
            articles.append(article)
        time.sleep(1)

    print('Generating ePub')
    ebook = EBookGenerator(title=filename)

    for article in articles:
        ebook.add_article(article)
        print(f'Appended {article.headline} to eBook')

    ebook.generate_ebook()
    print('Generated ePub')
    print(f'Sending eBook')
    server.send_email(filename=filename)

if __name__ == '__main__':
    try:
        main()
        print("Process completed successfully")
    except Exception as e:
        print(f"ERROR: Process failed: {e}")
        import traceback
        traceback.print_exc()