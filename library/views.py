from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from . import scray


# Create your views here.
def post_list(request):
  sc = scray.scray()
  sc_dic = { "key": sc }

  return render(request, 'library/library.html', sc_dic)