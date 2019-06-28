
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
import lxml


#"""

def NU():
    #Brill numen
    ID = 'NU'
    pub = 'Brill'
    j_url = "https://brill.com/view/journals/nu/nu-overview.xml"
    a_url = "https://brill.com/abstract/journals/nu/66/1/nu.66.issue-1.xml" 
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    HP = requests.get(a_url, headers=headers)
    HP_text = HP.text.split('strong')
    soup = BeautifulSoup(HP_text[0], 'lxml')
    soup2 = BeautifulSoup(HP.text, 'lxml')
    title = soup.find(class_="c-Button--link c-Button--primary").string
    #print(title)

    #論文タイトル
    NU_paper_titles = soup.find_all(class_="c-Typography c-Typography--title c-Button--link c-Button--primary")
    articles = []
    for NU_paper_title in NU_paper_titles:
        articles.append(NU_paper_title.getText().replace("\n","").strip(" "))
    articles.pop(-1)
    #print(articles)

    aa = NU_paper_titles
    urls = []
    for a in aa:
        b = a.get('href')
        c = "https://brill.com" + b
        urls.append(c)
    urls.pop(-1)
    #print(urls)

    image = soup2.find_all('img')
    for iimg in image:
        if '/cover' in iimg.get('src'):
            img = 'https://brill.com' +  iimg.get('src')
    
    
    area = 'Religion'
    authors = []
    auths = soup.find_all(class_="c-Button--link c-Button--primary")
    for auth in auths[1:]:
        authors.append(auth.getText())

    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls, "discipline":area, "authors":authors}
    return (context)

    
# MTSR----------------------------------------    
    
    
    
def MTSR():
    #Method & Theory in the Study of Religion
    ID = 'MTSR'
    pub = 'Brill'
    j_url = "https://brill.com/view/journals/mtsr/mtsr-overview.xml"
    a_url = "https://brill.com/abstract/journals/mtsr/31/2/mtsr.31.issue-2.xml"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    
    HP = requests.get(a_url, headers=headers)
    soup = BeautifulSoup(HP.text, 'lxml')
    title = soup.find(class_="c-Button--link c-Button--primary").string
    #print(title)

    #論文タイトル
    MTSR_paper_titles = soup.find_all(class_="c-Typography c-Typography--title c-Button--link c-Button--primary")
    articles = []
    for MTSR_paper_title in MTSR_paper_titles:
        if 'Advance Articles' in MTSR_paper_title.getText():
            break
        articles.append(MTSR_paper_title.getText().replace("\n","").strip(" "))
    #print(articles)

    aa = MTSR_paper_titles
    urls = []
    for a in aa:
        b = a.get('href')
        if 'aop' not in b:
            c = "https://brill.com" + b
        urls.append(c)
        #print(urls)

    image = soup.find_all('img')
    for iimg in image:
        if '/cover' in iimg.get('src'):
            img = 'https://brill.com' +  iimg.get('src')

    area = 'Religion'
    authors = []
    auths = soup.find_all(class_="c-Button--link c-Button--primary")
    for auth in auths[1:-1]:
        authors.append(auth.getText())   


    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls, "discipline":area, "authors":authors}
    return (context)
    
"""
context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls}
    return (context)
    
def NU_paper_titles():
    #Brill numen
    url = "https://brill.com/abstract/journals/nu/66/1/nu.66.issue-1.xml" 
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    HP = requests.get(url, headers=headers)
    soup = BeautifulSoup(HP.text, 'lxml')
    papers = soup.find_all(class_="title text-headline mb-3")
    
    #journalの名前
    issue = soup.find('h1').string
    title = soup.find(class_="c-Button--link c-Button--primary").string
    
    #論文タイトル
    nulists = soup.find_all(class_="c-Typography c-Typography--title c-Button--link c-Button--primary")
    list = []
    for nulist in nulists:
        nu_paper_titles = nulist.string
        if nu_paper_titles is None:
            break
        list.append(nu_paper_titles.replace("\n","").strip(" "))
   
    sublists = soup.find_all('div', attrs={'class':['subTitle', 'em']})
    list_2 = []
    for sublist in sublists:
        list_2.append(sublist.getText().replace("\n",""))
    context = {"NU":title,"NU_paper_titles":list,"NU_url":url, "subtitles":list_2}
    return (context)

# return (ID, title, j_url, img, pub, articles, urls)
"""