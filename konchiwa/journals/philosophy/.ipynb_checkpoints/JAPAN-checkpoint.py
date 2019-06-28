import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
import lxml

    
def Tetsu():

    ID = 'Tetsugaku'
    pub = '日本哲学会'
    j_url = "https://www.jstage.jst.go.jp/browse/philosophy/list/-char/ja" 
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    HP = requests.get(j_url, headers=headers)
    HP_text = (HP.text.split('応募論文'))
    soup = BeautifulSoup(HP_text[1], "html.parser")
    soup2 = BeautifulSoup(HP.text, "html.parser")


    #雑誌タイトル
    title = soup2.find("title").string

    #print(title)
    #論文タイトル
    aa = soup.find_all(class_="searchlist-title")
    articles = []
    for a in aa:
        articles.append(a.getText())
    #print(articles)

    #url
    urls = []
    bb = soup.find_all(class_="searchlist-title")
    for b in bb:
        cc = b.find_all('a')
        for c in cc:
            d = c.get('href')
            urls.append(d)
    #print(urls)
    img = 'https://www.kinokuniya.co.jp/images/goods/ar2/web/imgdata2/large/48628/4862859364.jpg'
    area = 'Philosophy'
    
    authors = []
    auths = soup.find_all(class_="searchlist-authortags customTooltip")
    for auth in auths:
        authors.append(auth.getText())
   
    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls, "discipline":area, "authors":authors}
    return (context)


    
def Ka_Tetsu():   
    ID = 'KaTetsu'
    pub = '日本科学哲学会'
    j_url = "https://www.jstage.jst.go.jp/browse/jpssj/list/-char/ja" 
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    HP = requests.get(j_url, headers=headers)
    HP_text = (HP.text.split('書評論文'))
    soup = BeautifulSoup(HP_text[0], "html.parser")
    soup2 = BeautifulSoup(HP.text, "html.parser")


    #雑誌タイトル
    title = soup2.find("title").string

    #print(title)
    #論文タイトル
    aa = soup.find_all(class_="searchlist-title")
    articles = []
    for a in aa:
        articles.append(a.getText())
    #print(articles)

    #url
    urls = []
    bb = soup.find_all(class_="searchlist-title")
    for b in bb:
        cc = b.find_all('a')
        for c in cc:
            d = c.get('href')
            urls.append(d)
    #print(urls)
    img = 'https://www1.e-hon.ne.jp/images/syoseki/ac_k/14/33838714.jpg'
    area = 'Philosophy'
   
    authors = []
    auths = soup.find_all(class_="searchlist-authortags customTooltip")
    for auth in auths:
        authors.append(auth.getText())
   
    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls, "discipline":area, "authors":authors}
    return (context)
