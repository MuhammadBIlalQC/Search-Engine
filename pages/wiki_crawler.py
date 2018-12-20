"""from bs4 import BeautifulSoup as BS4
import requests
from .info_retrieval import tokenizeAndSave



def runCrawler(start_link):
    links_crawled = []
    i = 0;
    def crawlLinks(start_link, i):
        req = requests.get(start_link)
        page = BS4(req.text, features="html.parser")
        text = getTextFromPage(page);
        tokenizeAndSave(text, start_link)
        for link in page.find_all('a'):
            href = str(link.get('href'))
            if 'https://en.wikipedia.org/' in href and href not in links_crawled and i < 4:
                links_crawled.append(href)
                print(href)
                crawlLinks(href, i = i + 1)

    crawlLinks(start_link)


def getTextFromPage(page):
    elems = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'p'];
    text_gathered = ""
    for elem in elems:
        text = ""
        try:
            text = page.find(elem).get_text()
        except Exception:
            print('Error')
        text_gathered += text;
    return text;
"""