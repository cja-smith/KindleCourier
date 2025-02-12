import json
import requests


class GuardianAPIClient:

    def __init__(self, api_key, edition='uk'):
        self.api_key = api_key
        self.edition = edition
        self.base_url = 'http://content.guardianapis.com'

    def get_top_story_urls(self):
        url = f'{self.base_url}/{self.edition}'

        params = {
            'api-key': self.api_key,
            'format': 'json',
            'show-editors-picks': 'true',
        }

        response = requests.get(url, params=params)

        # Ensure response is correct
        if not response.ok:
            response.raise_for_status()

        top_stories_json = response.json()

        return [article['apiUrl'] for article in top_stories_json['response']['editorsPicks']]

    def generate_article(self, article_url):

        params = {
            'api-key': self.api_key,
            'format': 'json',
            'show-fields': 'headline,trailText,body,byline,thumbnail',
        }

        response = requests.get(article_url,
                                params=params)

        if not response.ok:
            response.raise_for_status()

        data = response.json()['response']['content']

        if data['type'] == 'liveblog':
            return {
                'ignore': True
            }

        else:
            fields = data.get('fields', {})
            return {
                'headline': fields.get('headline', ''),
                'trailText': fields.get('trailText', ''),
                'byline': fields.get('byline', ''),
                'body': fields.get('body', ''),
                'thumbnail': fields.get('thumbnail', ''),
            }





# Move Article to own .py file
# NYT API start https://api.nytimes.com/svc/topstories/v2/home.json?api-key=yourkey