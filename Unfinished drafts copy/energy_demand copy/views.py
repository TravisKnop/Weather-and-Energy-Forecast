from django.shortcuts import render, render_to_response
import requests
from bs4 import BeautifulSoup


def home_view(request):
    data_set = []
    if request.GET:
        body = requests.get("https://webservices.iso-ne.com/api/v1.1/{}".GET.get('band')).content
    return render_to_response("home_view.html", {"data_set": data_set})
