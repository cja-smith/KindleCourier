from dotenv import load_dotenv
import os
from guardian_client import GuardianAPIClient
from models import Article


load_dotenv()

GUARDIAN_API_KEY = os.getenv('GUARDIAN_API_KEY')

api_client = GuardianAPIClient(api_key=GUARDIAN_API_KEY)


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
