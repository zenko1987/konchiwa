import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
import lxml

def CA():
    ID = 'CA'
    pub = 'The Society for Cultural Anthropology'
    j_url = "https://journal.culanth.org/index.php/ca" 
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    HP = requests.get(j_url, headers=headers)
    HP_text = HP.text.split("h2")
    soup = BeautifulSoup(HP.text, "html.parser")
    soup2 = BeautifulSoup(HP_text[8], "html.parser") 


    #雑誌タイトル
    title = 'Cultural Anthropology'

    #print(title)
    #論文タイトル
    aa = soup2.find_all("h3")
    articles = []
    for a in aa:
        articles.append(a.getText().replace('\n','').replace('\t',''))
    #print(articles)

    #url
    urls = []
    bb = soup2.find_all("h3")
    for b in bb:
        cc = b.find_all('a')
        for c in cc:
            d = c.get('href')
            urls.append(d)
    #print(urls)

    image = soup.find(class_="issue__cover")
    img = image.get('src')
    #print(img)
    area = 'Cultural Anthropology'

    authors = []
    abab = soup.find_all("div", class_="article_summary__content")
    for ab in abab:
        authors2 = []
        bb = ab.find_all(class_="name")
        for a in bb:   
            authors2.append(a.getText())
        b = ','.join(authors2)
        authors.append(b.replace('\n','').replace('\t',''))


    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls, "discipline":area, "authors":authors}
    return (context)
