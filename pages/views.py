from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import TermPosting
from .models import SearchResult
import requests
from bs4 import BeautifulSoup as BS4

# Create your views here.



def index(request):
    print(request.GET)
    return render(request, 'index.html')


def search(request):
    try:
        query = request.GET['query'];

        def searchQuery(query):
            terms = query.lower().split(' ')
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
                pass
                return
            return postingIntersection;

        links = searchQuery(query);
        results = getResultViews(links)
        print(results)
        return render(request, 'results.html', {'results': results, 'error': False})
    except Exception as e:
        return render(request, 'results.html', {'error': True})




def crawlLink(request):
    try:
        crawl = request.GET['link']
    except Exception as e:
        pass
    print('initiating crawl of URL ' + crawl)
    runCrawler(crawl)
    return HttpResponse('CRAWLING')


def tokenizeAndSave(docID, text):
    terms = text.lower().split(' ')
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
        retrievePageInfo(start_link, page)
        for link in page.find_all('a'):
            href = str(link.get('href'))
            if 'https' in href:
                print('crawling ' + href);
                crawlLinks(href)

    crawlLinks(start_link)


def getTextFromPage(page):
    html_elems = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'p'];
    text_gathered = ""
    for elem in html_elems:
        text = ""
        try:
            for html_element in page.find_all(elem):
                text += html_element.get_text()
        except Exception as e:
            pass
        text_gathered += text;
    return text;

def retrievePageInfo(link, page):
    if len(SearchResult.objects.filter(link=link)) != 0:
        return
    try:
        title = page.title.get_text()
        desc = ""
        for meta in page.find_all('meta'):
            if meta.get('name') == 'description':
                desc = meta.get('content')
        result = SearchResult(title=title, description=desc, link=link)
        result.save()
    except Exception:
        pass


def getResultViews(links):
    resultViews = [];
    for link in links:
        try:
            res = SearchResult.objects.filter(link=link)
            if len(res) != 0:
                resultViews.append(res[0])
        except Exception as e:
            pass
    return resultViews
