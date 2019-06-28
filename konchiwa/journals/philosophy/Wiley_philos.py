import requests
from bs4 import BeautifulSoup
import lxml
import re

#"""
def Nous():
    ID = 'Nous'
    pub = 'Wiley'
    j_url = "https://onlinelibrary.wiley.com/journal/14680068" 
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    HP = requests.get(j_url, headers=headers)
    soup = BeautifulSoup(HP.text, "html.parser")


    #雑誌タイトル
    title1 = soup.find("title").string
    title = title1[:title1.find("-")]

    #print(title)
    #論文タイトル
    aa = soup.find_all(class_="issue-item__title__en")
    articles = []
    for a in aa:
        articles.append(a.getText())
    #print(articles)
    #url
    urls = []
    bb = soup.find_all(class_="issue-item")
    for b in bb:
        cc = b.find_all('a')
        for c in cc:
            d = c.get('href')
            if 'epdf' in d:
                e = 'https://onlinelibrary.wiley.com' + d
                urls.append(e)
    #print(urls)

    image = soup.find(class_="cover-image__image hasDetails")
    imag = image.find('img')
    img = imag.get('src')
    #print(img)
    area = 'Philosophy'
   
    authors = []
    auths = soup.find_all("ul", class_="rlist--inline loa comma")
    for auth in auths:
        authors.append(auth.getText().strip().replace("\n", ', '))
    
    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls, "discipline":area, "authors":authors}
    return (context)





def PPR():
    ID = 'PPR'
    pub = 'Wiley'
    j_url = "https://onlinelibrary.wiley.com/journal/19331592" 
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    HP = requests.get(j_url, headers=headers)
    soup = BeautifulSoup(HP.text, "html.parser")


    #雑誌タイトル
    title1 = soup.find("title").string
    title = title1[:title1.find("-")]

    #print(title)
    #論文タイトル
    aa = soup.find_all(class_="issue-item__title__en")
    articles = []
    for a in aa:
        articles.append(a.getText())
    #print(articles)
    #url
    urls = []
    bb = soup.find_all(class_="issue-item")
    for b in bb:
        cc = b.find_all('a')
        for c in cc:
            d = c.get('href')
            if 'epdf' in d:
                e = 'https://onlinelibrary.wiley.com' + d
                urls.append(e)
    #print(urls)

    image = soup.find(class_="cover-image__image hasDetails")
    imag = image.find('img')
    img = imag.get('src')
    #print(img)

    area = 'Philosophy'
    authors = []
    auths = soup.find_all("ul", class_="rlist--inline loa comma")
    for auth in auths:
        authors.append(auth.getText().strip().replace("\n", ', '))
    
    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls, "discipline":area, "authors":authors}
    return (context)



def PhilosCompass():
    ID = 'PhilosCompass'
    pub = 'Wiley'
    j_url = "https://onlinelibrary.wiley.com/journal/17479991#pane-01cbe741-499a-4611-874e-1061f1f4679e01" 
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    HP = requests.get(j_url, headers=headers)
    soup = BeautifulSoup(HP.text, "html.parser")


    #雑誌タイトル
    title1 = soup.find("title").string
    title = title1[:title1.find("-")]

    #print(title)
    #論文タイトル
    aa = soup.find_all(class_="issue-item__title__en")
    articles = []
    for a in aa:
        articles.append(a.getText())
    #print(articles)
    #url
    urls = []
    bb = soup.find_all(class_="issue-item")
    for b in bb:
        cc = b.find_all('a')
        for c in cc:
            d = c.get('href')
            if 'epdf' in d:
                e = 'https://onlinelibrary.wiley.com' + d
                urls.append(e)
    #print(urls)

    image = soup.find(class_="cover-image__image hasDetails")
    imag = image.find('img')
    img = imag.get('src')
    #print(img)

    area = 'Philosophy'
   
    authors = []
    auths = soup.find_all("ul", class_="rlist--inline loa comma")
    for auth in auths:
        authors.append(auth.getText().strip().replace("\n", ', '))
    
    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls, "discipline":area, "authors":authors}
    return (context)


def J_Appl_Philos():
    ID = 'J_Appl_Philos'
    pub = 'Wiley'
    j_url = "https://onlinelibrary.wiley.com/journal/14685930" 
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    HP = requests.get(j_url, headers=headers)
    soup = BeautifulSoup(HP.text, "html.parser")


    #雑誌タイトル
    title1 = soup.find("title").string
    title = title1[:title1.find("-")]

    #print(title)
    #論文タイトル
    aa = soup.find_all(class_="issue-item__title__en")
    articles = []
    for a in aa:
        articles.append(a.getText())
    #print(articles)
    #url
    urls = []
    bb = soup.find_all(class_="issue-item")
    for b in bb:
        cc = b.find_all('a')
        for c in cc:
            d = c.get('href')
            if 'epdf' in d:
                e = 'https://onlinelibrary.wiley.com' + d
                urls.append(e)
    #print(urls)

    image = soup.find(class_="cover-image__image hasDetails")
    imag = image.find('img')
    img = imag.get('src')
    #print(img)

    area = 'Philosophy'
   
    authors = []
    auths = soup.find_all("ul", class_="rlist--inline loa comma")
    for auth in auths:
        authors.append(auth.getText().strip().replace("\n", ', '))
    
    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls, "discipline":area, "authors":authors}
    return (context)
    
    
#"""