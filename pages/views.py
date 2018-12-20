from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import TermPosting
import requests
from bs4 import BeautifulSoup as BS4

# Create your views here.

from .wiki_crawler import *


def index(request):
    print(request.GET)
    return render(request, 'index.html')


def search(request):
    try:
        query = request.GET['query'];

        def searchQuery(query):
            terms = query.split(' ')
            postings = dict();
            for term in terms:
                termPostings = TermPosting.objects.filter(term=term)
                termPostings = list(termPostings);
                for termPosting in termPostings:
                    if postings.get(termPosting.term) == None:
                        postings[termPosting.term] = [termPosting.docID]
                    else:
                        if termPosting.docID not in postings[termPosting.term]:
                            postings[termPosting.term].append(termPosting.docID);
            try:
                postingIntersection = set(postings[terms[0]]);

                for i in range(1, len(terms)):

                    postingIntersection = postingIntersection.intersection(postings[terms[i]]);
            except Exception as e:
                print('made an error at intersect')
                return
            return postingIntersection;

        results = searchQuery(query);
        return render(request, 'results.html', {'links': results});
    except Exception as e:
        print(query.split(' '))
        return HttpResponse(e);



def start(request):

    try:
        crawl = request.GET['crawl']
        crawlLink = request.GET['crawl']
    except Exception:
        print(Exception)


    def tokenizeAndSave(docID, text):
        terms = text.split(' ')
        for term in terms:
            termPosting = TermPosting(term=term, docID=docID)
            termPosting.save()

    def runCrawler(start_link):
        links_crawled = []
        i = 0;

        def crawlLinks(start_link):
            req = requests.get(start_link)
            page = BS4(req.text, features="html.parser")
            text = getTextFromPage(page);
            tokenizeAndSave(start_link, text)
            for link in page.find_all('a'):
                href = str(link.get('href'))
                if 'https' in href and href not in links_crawled:
                    print('crawling ' + href);
                    links_crawled.append(href)
                    crawlLinks(href)

        crawlLinks(start_link)

    def getTextFromPage(page):
        elems = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'p'];
        text_gathered = ""
        for elem in elems:
            text = ""
            try:
                text = page.find(elem).get_text()
            except Exception as e:
                print(e)
            text_gathered += text;
        return text;

    runCrawler('https://www.google.com/search?q=microsoft&rlz=1C1CHBF_enUS761US761&oq=microsoft&aqs=chrome..69i57j69i61l3j0j69i59.2401j0j7&sourceid=chrome&ie=UTF-8')
    return HttpResponse('CRAWLING')