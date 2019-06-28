import sys
import os
import django

import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import article


os.environ.setdefault("DJANGO_SETTINGS_MODULE","ohayo.settings")
 
django.setup()

from konchiwa.models import article

def save_HR_paper_titles():
    url = "https://www.journals.uchicago.edu/toc/hr/current" 
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    HP = requests.get(url, headers=headers)
    soup = BeautifulSoup(HP.text, "html.parser")
    #雑誌のタイトル
    publisher = soup.find_all(class_="menu-section")[1].string
    title = soup.find('em').string

    #論文のタイトル
    papers = soup.find_all(class_="hlFld-Title")
    list = []
    for paper in papers [2:]:
        if "<i>" not in str(paper):
            paper_titles = paper.getText()
            if not article.objects.filter(title=paper_titles):
                list.append(article(title=paper_titles))
    paper_titles.objects.bulk_create(list)
