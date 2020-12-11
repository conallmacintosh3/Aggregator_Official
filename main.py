from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time


class AggregatorChrome:
    key_words = []
    links_of_articles = []
    picked_articles = []

    def __init__(self, link):
        self.link = link
        self.article = None
        self.articles = None
        self.word = None

        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(self.link)

        self.get_article()

        # QUIT THE DRIVER AT END OF SESSION
        self.driver.quit()

    def scroll(self, max_times=0):
        """
        Scrolls down on the webpage if it is needed
        :param max_times: The number of times the webpage is to be scrolled,
            by default this value is set to 0
        """
        # Number of times to scroll
        page = 0

        # Get scroll height
        last_height = self.driver.execute_script('return document.body.scrollHeight')

        while page < max_times:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

            # Wait 1 second
            time.sleep(2)

            # Calc new scroll height and compare with last
            new_height = self.driver.execute_script('return document.body.scrollHeight')
            if new_height == last_height:
                break
            last_height = new_height

    def get_article(self, class_=None):
        """
        Searches the given webpage for articles that contain a keyword `key_words`
        """
        articles = self.driver.find_elements_by_class_name(class_)

        for article in articles:
            self.article = article
            for word in self.key_words:
                if word in self.article.text:
                    self.word = word
                    if self.filter():
                        self.get_article_link()

    def get_article_link(self):
        """
        In conjunction with the `get_article` method, it will get the link
        for the article that contains the key word in `key_words`
        :return: link
        """
        link = self.article.get_attribute('href')
        if link is None:
            pass

        self.links_of_articles.append(link)
        return link

    def filter(self):
        if self.word in [x for x in self.picked_articles]:
            return False
        else:
            self.picked_articles.append(self.word)
            return True


class AggregatorFirefox:
    key_words = []
    links_of_articles = []
    picked_articles = []

    def __init__(self, link):
        from selenium.webdriver.firefox.options import Options

        self.link = link
        self.article = None
        self.articles = None
        self.word = None

        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.get(self.link)

        self.get_article()

        # QUIT THE DRIVER AT END OF SESSION
        self.driver.quit()

    def scroll(self, max_times=0):
        """
        Scrolls down on the webpage if it is needed
        :param max_times: The number of times the webpage is to be scrolled,
            by default this value is set to 0
        """
        # Number of times to scroll
        page = 0

        # Get scroll height
        last_height = self.driver.execute_script('return document.body.scrollHeight')

        while page < max_times:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

            # Wait 1 second
            time.sleep(2)

            # Calc new scroll height and compare with last
            new_height = self.driver.execute_script('return document.body.scrollHeight')
            if new_height == last_height:
                break
            last_height = new_height

    def get_article(self, class_=None):
        """
        Searches the given webpage for articles that contain a keyword `key_words`
        """
        articles = self.driver.find_elements_by_class_name(class_)

        for article in articles:
            self.article = article
            for word in self.key_words:
                if word in self.article.text:
                    self.word = word
                    if self.filter() is True:
                        self.get_article_link()

    def get_article_link(self):
        """
        In conjunction with the `get_article` method, it will get the link
        for the article that contains the key word in `key_words`
        :return: link
        """
        link = self.article.get_attribute('href')
        if link is None:
            pass

        self.links_of_articles.append(link)
        return link

    def filter(self):
        if self.word in [x for x in self.picked_articles]:
            return False
        else:
            self.picked_articles.append(self.word)
            return True


class CBC(AggregatorFirefox):
    key_words = ['COVID-19', 'climate', "Space X", "self-driving", "Ontario"]

    def __init__(self, link):
        super().__init__(link)

    def get_article(self, class_='contentWrapper'):
        articles = self.driver.find_elements_by_class_name(class_)

        for article in articles:
            self.article = article
            for word in self.key_words:
                if word in self.article.text:
                    if self.filter():
                        a = self.article.find_element_by_class_name('headline').text
                        self.get_article_link()

    def filter(self):
        for word in self.article.find_element_by_class_name('headline').text:
            if word in [x for x in self.picked_articles]:
                return False
            else:
                return True


class CNBC(AggregatorChrome):
    key_words = ["Tesla", "IPO", "Amazon", "Elon Musk", "self-driving", "artificial"]

    def __init__(self, link):
        super().__init__(link)

    def get_article(self, class_='Card-titleContainer'):
        super().get_article(class_)

    def get_article_link(self):
        element = self.article.find_element_by_css_selector("div.Card-titleContainer > a")
        link = element.get_attribute("href")
        if link is None:
            pass

        self.links_of_articles.append(link)
        return link

    def check_duplicates(self):
        pass


class ScienceDaily(AggregatorChrome):
    key_words = ["Solar", "Meteor", "Galaxy"]

    def __init__(self, link):
        super().__init__(link)

    def get_article(self, class_='latest-head'):
        super().get_article(class_)

    def get_article_link(self):
        element = self.article.find_element_by_css_selector("h3.latest-head > a")
        link = element.get_attribute("href")
        if link is None:
            pass

        self.links_of_articles.append(link)
        return link


class ScienceNews(AggregatorChrome):
    key_words = ["ancient", "Ancient", "fire", "hurricane", "climate"]

    def __init__(self, link):
        super().__init__(link)

    def get_article(self, class_='post-item-river__title___J3spU'):
        super().get_article(class_)

    def get_article_link(self):
        element = self.article.find_element_by_css_selector("h3.post-item-river__title___J3spU > a")
        link = element.get_attribute("href")
        if link is None:
            pass

        self.links_of_articles.append(link)
        return link


class TechCrunch(AggregatorChrome):
    key_words = ["SpaceX", "Space", "Nasa", "NASA"]

    def __init__(self, link):
        super().__init__(link)

    def get_article(self, class_='post-block__title__link'):
        super().get_article(class_)
