from main import *
from article_summarize import NewsPage
from send_email import email

from urls import cbc, cnbc, science_news, science_daily, tech_crunch


def get_articles(urls_name, class_name):
    for index, link in enumerate(urls_name):
        print(f"Articles from the link {link}")
        class_name(urls_name[index])
    print(f"Total Links: {len(class_name.links_of_articles)}")
    print("-" * 40)


def main():
    # TIME
    start = time.time()

    # GET ALL THE ARTICLE LINKS
    # CBC
    get_articles(cbc, CBC)

    # CNBC
    get_articles(cnbc, CNBC)

    # ScienceDaily
    get_articles(science_daily, ScienceDaily)

    # ScienceNews
    get_articles(science_news, ScienceNews)

    # TechCrunch
    get_articles(tech_crunch, TechCrunch)

    # PRINT OUT THE SUMMARIZATION OF EACH ARTICLE
    NewsPage.clear_storage()
    for href in AggregatorFirefox.links_of_articles:
        NewsPage(href)

    for href in AggregatorChrome.links_of_articles:
        NewsPage(href)

    # CALCULATE ELAPSED TIME
    end = time.time()
    print(f"Elapsed time: {end - start}")

    # SEND THE EMAIL FROM ARTICLE_STORAGE.TXT
    email()


if __name__ == '__main__':
    main()
    # time.sleep(30)
