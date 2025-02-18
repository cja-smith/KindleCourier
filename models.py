class Article:

    def __init__(self, headline, trailText, byline, body, thumbnail):
        self.headline = headline
        self.trailText = trailText
        self.byline = byline
        self.body = body
        self.thumbnail = thumbnail

    def to_html(self):
        html=(f'<h1>{self.headline}</h1>\n'
              f'<h2>{self.trailText}</h2>\n'
              f'<h3>{self.byline}</h3>\n'
              f'<h2>{self.thumbnail}</h2>\n\n'
              f'{self.body}'
              )

        return html