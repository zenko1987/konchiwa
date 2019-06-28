import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


def HR_titles():
    ID = 'HR'
    j_url = "https://www.journals.uchicago.edu/toc/hr/current" 
    headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
            }
    HP = requests.get(j_url, headers=headers)
    HP_text = HP.text.split('Book Reviews')
    soup = BeautifulSoup(HP_text[0], "html.parser")
    
    #雑誌のタイトル
    publisher = soup.find_all(class_="menu-section")[1].string
    title = soup.find('em').string
    #return (title)

    #論文のタイトル
    articles = []
    papers = soup.find_all(class_="hlFld-Title")
    for paper in papers[2:]:
        paper_titles = paper.getText()
        articles.append(paper_titles)
    #return (list)

    #論文のURL    
    urls = []
    aa = soup.find_all('a', class_="ref nowrap")
    for a in aa[2:]:
        b = a.get('href')
        if "/abs" in b:
            urls_list = "https://www.journals.uchicago.edu" + b
            urls.append(urls_list)
    
    #表紙画像
    image = soup.find('img', alt="Publication Cover")
    img_url = image.get("src")
    img = "https://www.journals.uchicago.edu" + img_url
    
    p = soup.find_all(class_="menu-section")
    pub = p[1].string
        
    area = 'Religion'
   
    authors = []
    abab = soup.find_all("tr")
    for ab in abab:
        authors2 = []
        bb = ab.find_all(class_="hlFld-ContribAuthor")
        for a in bb:   
            authors2.append(a.getText())
        b = ','.join(authors2)
        authors.append(b)
    authors = list(filter(lambda str:str != '', authors))

    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls, "discipline":area, "authors":authors}
    return (context)
"""        
    context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls}
    return (context)
    
    
    

    





HR = HR_chicago.HR_titles()

j = HR
Journal.objects.get_or_create(
    journal_ID = j[0], #ID,
    journal = j[1], #title,
    URL = j[2], #j_url,
    image = j[3], #img,
    publisher = j[4] #pub,
    )   
                                     

for (article, url) in zip(j[5], j[6]):
    Article.objects.get_or_create(
        article = article, 
        URL = url, 
        journal_ID = j[0], #ID,
        year = '2019', 
        month = 'May'
    )

"""

















"""
def HR_paper_titles():
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
            list.append(paper_titles)
    context = {"HR":title,"CUP":publisher,"HR_paper_titles":list,"HR_url":url}
    return (context)
"""