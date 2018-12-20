from django.contrib import admin
from .models import TermPosting
from .models import SearchResult

# Register your models here.
admin.site.register(TermPosting)
admin.site.register(SearchResult)