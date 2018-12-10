import os
try:
    from .wiki_crawler import runCrawler
except Exception:
    from wiki_crawler import runCrawler

def runWikiCrawler():
    start_link = 'https://en.wikipedia.org/wiki/Wikipedia'
    runCrawler(start_link)
    

child = os.fork()
if child == 0:
    runWikiCrawler()
