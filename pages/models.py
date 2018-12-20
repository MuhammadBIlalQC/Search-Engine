from django.db import models
# Create your models here.


class TermPosting(models.Model):
    term = models.CharField(max_length=30)
    docID = models.CharField(max_length=100)

    def __str__(self):
        return self.docID


class SearchResult(models.Model):
    title = models.CharField(max_length=30)
    link = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
