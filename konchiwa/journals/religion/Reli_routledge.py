import requests
from bs4 import BeautifulSoup
import lxml
import re

def Reli_paper_titles():
    ID = 'Reli'
    pub = 'Routledge'
    j_url = "https://www.tandfonline.com/toc/rrel20/current"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    HP = requests.get(j_url, headers=headers)
    HP_text = HP.text.split('Book Reviews')
    soup = BeautifulSoup(HP.text, "html.parser")
    soup2 = BeautifulSoup(HP_text[0], "html.parser")


    #ジャーナルタイトル
    title = soup.find(class_="title").string
    #print(title)

    #論文タイトル
    articles = []
    p_titles = soup2.find_all(class_="art_title linkable")
    for p_title in p_titles:
        articles.append(p_title.getText())
    
    urls = []
    for p_title in p_titles:
        b = p_title.find('a').get('href')
        c = 'https://www.tandfonline.com' + b
        urls.append(c)
    #print(urls)

    authors = []
    abab = soup2.find_all(class_="articleEntryAuthor all")
    for ab in abab:
        authors.append(ab.getText().replace("\n",''))
    

    image = soup.find(class_="publicationCoverImage")
    imag = image.find('img').get('src')
    img = 'https://www.tandfonline.com' + imag
    #print(img)  
    

    area = 'Religion'
    
    
    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls, "discipline":area, "authors":authors}
    return (context)











  
    
 
"""   
   context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls}
    return (context)
    



def Reli_paper_titles():
    #Routledge religion
    url = "https://www.tandfonline.com/toc/rrel20/current"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
    HP = requests.get(url, headers=headers)
    soup = BeautifulSoup(HP.text, 'lxml')
    #ジャーナルタイトル
    papers = soup.find(class_="title").string
    
    #論文タイトル
    list = []
    p_titles = soup.find_all(class_="header")
    for p_title in p_titles:
        aaa = p_title.getText()
        if 'Article' in aaa:
            Reli_titles = aaa.replace("Article",'').replace("\n","").strip(" ")
            list.append(Reli_titles)
    context = {"Reli":papers,"Reli_paper_titles":list,"Reli_url":url}
    return (context)
   
"""