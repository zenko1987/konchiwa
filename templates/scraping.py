import requests
from bs4 import BeautifulSoup

def paper_titles(site):
    #シカゴ　Historyo of religions
    url = site 
    HP = requests.get(url)
    soup = BeautifulSoup(HP.text, "html.parser")
    papers = soup.find_all(class_="hlFld-Title")

    #journalの名前
    print(soup.find("title").getText())

    #論文の名前
    del papers[0:2]
    for paper in papers:
        colum = ":"
        main = paper.getText()[:paper.getText().find(colum)]
        if "," not in main:
            print(paper.getText())
                
paper_titles("https://www.journals.uchicago.edu/toc/hr/current")

