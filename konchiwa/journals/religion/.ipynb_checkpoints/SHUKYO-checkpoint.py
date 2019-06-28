import requests
from bs4 import BeautifulSoup
import lxml
import re


def Shukyo():
    ID = 'SHUKYO'
    pub = '日本宗教学会'
    j_url = "https://www.jstage.jst.go.jp/browse/rsjars/list/-char/ja" 
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    HP = requests.get(j_url, headers=headers)
    HP_text = HP.text.split('書評と紹介')
    soup = BeautifulSoup(HP_text[0], "html.parser")

    #雑誌タイトル
    title = soup.find("title").string
    
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
    img = 'http://jpars.org/journal/database/wp-content/uploads/2014/02/vol1_no1.gif'

    area = 'Religion'
    
    authors = []
    auths = soup.find_all(class_="searchlist-authortags customTooltip")
    for auth in auths:
        authors.append(auth.getText())
    authors = list(filter(lambda str:str != '', authors))
    
    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls, "discipline":area, "authors":authors}
    return (context)
#return (ID, title, j_url, img, pub, articles, urls)


def ShuSya():
    ID = 'SHU_SYA'
    pub = '「宗教と社会」学会'
    j_url = "https://www.jstage.jst.go.jp/browse/religionandsociety/list/-char/ja" 
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    HP = requests.get(j_url, headers=headers)
    HP_text = HP.text.split("研究ノート")
    soup = BeautifulSoup(HP_text[0], "html.parser")
    soup2  = BeautifulSoup(HP.text, "html.parser")

    #雑誌タイトル
    title = soup2.find("title").string

    #print(title)
    #論文タイトル
    aa = soup.find_all(class_="searchlist-title")
    articles = []
    for a in aa[2:]:
        articles.append(a.getText())
    #print(articles)

    #url
    urls = []
    bb = soup.find_all(class_="searchlist-title")
    for b in bb[2:]:
        cc = b.find_all('a')
        for c in cc:
            d = c.get('href')
            urls.append(d)
    #print(urls)
    img = 'https://www.jstage.jst.go.jp/pub/religionandsociety/thumbnail/religionandsociety_22.png'

    area = 'Religion'
   
    authors = []
    auths = soup.find_all(class_="searchlist-authortags customTooltip")
    for auth in auths:
        authors.append(auth.getText())
   
    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls, "discipline":area, "authors":authors}
    return (context)
