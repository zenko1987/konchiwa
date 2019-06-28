import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
import lxml



def PhilosRev():
    ID = 'PhilosRev'
    pub = 'Duke University Press'
    j_url = "https://read.dukeupress.edu/the-philosophical-review/issue/128/1" 
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    HP = requests.get(j_url, headers=headers)
    soup = BeautifulSoup(HP.text, "html.parser")


    #雑誌タイトル
    title = "The Philosophical Review"
    #print(title)
    #論文タイトル
    aa = soup.find_all(class_="customLink item-title")
    articles = []
    for a in aa:
        articles.append(a.getText().replace("\n","").strip(" "))
    #print(articles)
    #url
    urls = []
    bb = soup.find_all(class_="customLink item-title")
    for b in bb:
        cc = b.find_all('a')
        for c in cc:
            d = c.get('href')
            e = 'https://read.dukeupress.edu' + d
            urls.append(e)
    #print(urls)

    #image = soup.find(class_="fb-featured-image")
    #img = image.get('src')
    img =''
    
    area = 'Philosophy'
    
    authors = []
    auths = soup.find_all(class_="al-authors-list")
    for auth in auths:
        authors.append(auth.getText().strip())
   
    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls, "discipline":area, "authors":authors}
    return (context)
    #context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls}
    #return (context)