import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
import lxml

def CRR():
    ID = 'CRR'
    pub = 'SAGE'
    j_url = "https://journals.sagepub.com/toc/crra/7/1" 
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    HP = requests.get(j_url, headers=headers)
    HP_text = HP.text.split('Book Reviews')
    soup = BeautifulSoup(HP.text, "html.parser")
    soup2 = BeautifulSoup(HP_text[0+1], "html.parser")

    #雑誌タイトル
    title1 = soup.find("title").string
    title = title1[:title1.find("-")]
    #出版社
    pub = soup.find(class_="copyrightSAGELink").getText()
    #論文タイトル
    aa = soup2.find_all(class_="heading-title")
    articles = []
    for a in aa:
        articles.append(a.getText())

    #url
    urls = []
    bb = soup2.find_all('div', class_="art_title linkable")
    for b in bb:
        cc = b.find_all('a')
        for c in cc:
            d = c.get('href')
            e = 'https://journals.sagepub.com' + d
            urls.append(e)

    image = soup.find(class_="cover")
    imag = image.find('img')
    img = 'https://journals.sagepub.com' + imag.get('src')

    area = 'Religion'
    
    authors = []
    auths = soup2.find_all(class_="articleEntryAuthor all")
    for auth in auths:
        authors2 = []
        au = auth.find_all(class_="header")
        for a in au:
            authors2.append(a.getText().replace("Search Google Scholar",'').replace("for this author",'').replace("See all articles by this author",''))
            b = ','.join(authors2)
        authors.append(b)
   
    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls, "discipline":area, "authors":authors}
    return (context)


    
    """    
    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls}
    return (context)




return (ID, title, j_url, img, pub, articles, urls)



def CRR():
    #SEGE Critical Research of Relgion 
    url = "https://journals.sagepub.com/toc/crra/7/1" 
    HP = requests.get(url)
    soup = BeautifulSoup(HP.text, "html.parser")
    aa = soup.find_all(class_="heading-title")
    #雑誌タイトル
    title = soup.find("title").string
    title_text = title[:title.find("-")]
    #出版社
    pub = soup.find(class_="copyrightSAGELink").getText()
    #論文タイトル
    list = []
    for a in aa:
        colum = ":"
        main = a.getText()[:a.getText().find(colum)]
        if "," not in main:
            list.append(a.getText())
    context = {"CRR":title_text,"CRR_pub":pub,"CRR_paper_titles":list,"CRR_url":url}
    return (context)
   
"""                      
    
 
