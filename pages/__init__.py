import os
from .wiki_crawler import runCrawler


def runWikiCrawler():
    start_link = 'https://en.wikipedia.org/wiki/Wikipedia'
    runCrawler(start_link)
#runWikiCrawler();

#child = os.fork()
#if child == 0:
    #runWikiCrawler()
