from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
def index(request):
    print(request.GET)
    return render(request, 'index.html')

def search(request):
    query = request.GET['query']
    return HttpResponse("SEARCHING")