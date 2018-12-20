from .models import TermPosting


def tokenizeAndSave(docID, text):
    terms = text.split(' ')
    for term in terms:
        termPosting = TermPosting(term=term, docID=docID)
        termPosting.save()
