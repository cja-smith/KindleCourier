from ebooklib import epub
import os
from models import Article


class EBookGenerator:
    def __init__(self,title='KindleCourier.epub',author='Various Writers'):
        self.book=epub.EpubBook()
        self.book.set_title(title)
        self.book.set_language('en')
        self.output_path=os.path.join(os.getcwd(),'attachments',f'{title}')

        self.book.add_author(author)

    def add_article(self, article: Article):
        # Takes data from Article class object, and adds to EpubBook instance
        # Need to find an alternate way to add in thumbnails
        chapter=epub.EpubHtml(title=f'{article.headline}',
                              file_name=f'{article.headline}.xhtml',)
        chapter.set_content(f'{article.to_html()}')
        self.book.add_item(chapter)

        return f'{chapter.file_name} successfully added to {self.book.title}'

    def generate_toc(self):
        toc = []
        for chapter in self.book.get_items_of_type(epub.EpubHtml):
            # Ensure that the title is a valid string
            toc.append((chapter.title, chapter.file_name))
        return tuple(toc)


    def generate_ebook(self):
        # Generate Table of Contents
        print('Generating TOC')
        self.book.toc = self.generate_toc()
        print(self.generate_toc())
        # Creates spine
        chapters=[chapter for chapter in self.book.items]
        chapters.insert(0, 'nav')
        self.book.spine = chapters

        self.book.add_item(epub.EpubNcx())
        self.book.add_item(epub.EpubNav())

        epub.write_epub(self.output_path, self.book)