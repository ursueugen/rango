from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse(
        "<p>Hey django partner!</p>"
        "<a href='/rango/about/'>Link to about</a>"
    )

def about(request):
    return HttpResponse(
        "<p>This is the about page!</p>"
        "<a href='/rango/'>Link to index</a>"
    )