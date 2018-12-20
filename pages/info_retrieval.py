"""
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

import time
try:
    from pages.models import TermPosting
except Exception:
    def ready(self):
        # importing model classes
        from .models import TermPosting  # or...

        # registering signals with the model's string label
        pre_save.connect(receiver, sender='pages.TermPosting')

def tokenizeAndSave(docID, text):
    terms = text.split(' ')
    for term in terms:
        termPosting = TermPosting(term=term, docID=docID)
        termPosting.save()
"""