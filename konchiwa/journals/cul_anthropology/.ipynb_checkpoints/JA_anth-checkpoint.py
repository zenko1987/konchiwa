import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
import lxml

    
def Bunka_jinrui():

    ID = 'Bunka_jinrui'
    pub = '日本文化人類学会'
    j_url = "https://www.jstage.jst.go.jp/browse/jjcanth/list/-char/ja" 
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    HP = requests.get(j_url, headers=headers)
    HP_text = (HP.text.split('特集'))
    soup = BeautifulSoup(HP_text[0], "html.parser")
    soup2 = BeautifulSoup(HP.text, "html.parser")


    #雑誌タイトル
    title = soup2.find("title").string

    #print(title)
    #論文タイトル
    aa = soup.find_all(class_="searchlist-title")
    articles = []
    for a in aa[5:]:
        articles.append(a.getText())
    #print(articles)

    #url
    urls = []
    bb = soup.find_all(class_="searchlist-title")
    for b in bb[5:]:
        cc = b.find_all('a')
        for c in cc:
            d = c.get('href')
            urls.append(d)
    #print(urls)

    img = 'http://www.jasca.org/publication/jjca/img/jjca.81.1.gif'
    area = 'Cultural Anthropology'
   
    authors = []
    auths = soup.find_all(class_="searchlist-authortags customTooltip")
    for auth in auths:
        authors.append(auth.getText())
    authors = list(filter(lambda str:str != '', authors))
    

    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls, "discipline":area, "authors":authors}
    return (context)
