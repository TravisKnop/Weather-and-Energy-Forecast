from django.shortcuts import render
from bs4 import BeautifulSoup

from weather_data.models import Weather

def hello(request):
    date_links = []
    if request.GET:
        body = requests.get("")