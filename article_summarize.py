from newspaper import Article

# from main import *
# import nltk

article_num = 0


class NewsPage:

    def __init__(self, url):
        self.url = url
        self.article = None

        self.get_news_page_links()

    def get_news_page_links(self):
        self.article = Article(self.url)
        self.download()
        self.get_summary()

    def download(self):
        # Download the HTML
        self.article.download()
        # Parse the HTML
        self.article.parse()
        # Perform Natural Language Processing
        self.article.nlp()

    @staticmethod
    def clear_storage():
        with open("article_storage.txt", 'w') as f:
            f.write('')

    def get_summary(self):
        """
        gets the headline, data, summary, and link from the article
        and writes the information into a text file (with formatting)
        """
        with open("article_storage.txt", 'a') as a:
            a.write(("-" * 40) + "\n")
            a.write(self.article.title + ("\n" * 2))
            if self.article.publish_date is None:
                a.write("DATE NOT FOUND" + ("\n" * 2))
            else:
                a.write(str(self.article.publish_date).split()[0] + ("\n" * 2))
            a.write(self.article.summary + ("\n" * 2))
            a.write(self.url + ("\n" * 2))
