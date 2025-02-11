guardian_api_key = open("guardian_api.txt").read().strip()
api_client = GuardianAPIClient(api_key=guardian_api_key)

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