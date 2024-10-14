from django.shortcuts import render
from django.http import HttpResponse
import requests

from .models import Greeting

# Create your views here.

def index(request):
    r = requests.get('https://httpbin.org/status/418')
    print(r.text)  # This will log the response text to your console
    return HttpResponse('<pre>' + r.text + '</pre>')

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
import os
from django.http import HttpResponse
def index(request):
    times = int(os.environ.get('TIMES', 3))
    return HttpResponse('Hello! ' * times)