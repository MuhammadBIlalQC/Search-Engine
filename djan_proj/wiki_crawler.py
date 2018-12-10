from bs4 import BeautifulSoup as BS4
import requests

def runCrawler(start_link):
    links_crawled = []

    def crawlLinks(start_link):
        req = requests.get(start_link)
        page = BS4(req.text, features="html.parser")
        for link in page.find_all('a'):
            href = str(link.get('href'))
            if 'https://en.wikipedia.org/' in href and href not in links_crawled:
                links_crawled.append(href)
                print(href)
                crawlLinks(href)
    
    crawlLinks(start_link)

