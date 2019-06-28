"""   
#上記モデルの取り込み    
from konchiwa.models import Journal
from konchiwa.models import Article

#宗教 
from konchiwa.journals.religion import HR_chicago
from konchiwa.journals.religion import HR_chicago
from konchiwa.journals.religion import Religion_brill
from konchiwa.journals.religion import Reli_routledge
from konchiwa.journals.religion import religion_sage
from konchiwa.journals.religion import SHUKYO
from konchiwa.journals.religion import SHU_SYA

#論文リストの取り込み
SHUKYO = SHUKYO.Shukyo()
SHU_SYA = SHU_SYA.ShuSya()
NU = Religion_brill.NU()
Reli = Reli_routledge.Reli_paper_titles()
MTSR = Religion_brill.MTSR()
CRR = religion_sage.CRR()
HR = HR_chicago.HR_titles()
#title, articles, urls, j_url, img, pub 
#ID[0], title[1], j_url[2], img[3], pub[4], articles[5], urls[6] = HR_chicago.HR_titles()


#哲学
from konchiwa.journals.philosophy import PhilosRev
from konchiwa.journals.philosophy import Wiley_philos
from konchiwa.journals.philosophy import JAPAN


PhilosRev = PhilosRev.PhilosRev()
Nous = Wiley_philos.Nous()
PPR = Wiley_philos.PPR()
PhilosCompass = Wiley_philos.PhilosCompass()
J_Appl_Philos = Wiley_philos.J_Appl_Philos()
Tetsu = JAPAN.Tetsu()
KaTetsu = JAPAN.Ka_Tetsu()



#文化人類学
from konchiwa.journals.cul_anthropology import CA
from konchiwa.journals.cul_anthropology import CA_sage

CA = CA.CA()
Anthropol_Theory = CA_sage.Anthropol_Theory()

# CAとった
j = [CA, HR, Reli, SHU_SYA, SHUKYO, CRR, NU, MTSR, KaTetsu, Tetsu, PPR, Nous, PhilosCompass, PhilosRev, J_Appl_Philos, Anthropol_Theory]


#-------------------Journal-----------------
#ID
def ID():
    IDs = [d.get("ID") for d in j]
    for ID in IDs:
        return (ID)


#title
def title():
    titles = [d.get("title") for d in j]
    for title in titles:
        return (title)

#j_url
def j_url():
    j_urls = [d.get("j_url") for d in j]
    for j_url in j_urls:
        return (j_url)

#image
def image():
    images = [d.get("img") for d in j]
    for image in images:
        return (image)

#publisher
def publisher():
    publishers = [d.get("pub") for d in j]
    for publisher in publishers:
        return (publisher)

    
#-------------------Article-----------------

#article
def article():
    articleb = []
    articles = [d.get("articles") for d in j]
    for articlea in articles:
        articleb.append(articlea)
        for article in articleb:
            return (article)

#url
def url():
    urlb = []
    urls = [d.get("url") for d in j]
    for urla in urls:
        urlb.append(urla)
        for url in urlb:
            return (url)

""" 
""" 
Journal.objects.get_or_create(URL = j_url)


#image
images = [d.get("img") for d in j]
for image in images:
    Journal.objects.get_or_create(iamge = image)

#publisher
publishers = [d.get("pub") for d in j]
for publisher in publishers:
    Journal.objects.get_or_create(publisher = publisher)

#----------Article------------
#article
articles = [d.get("articles") for d in j]
for article in articles:
    Article.objects.get_or_create(article = article)





    Journal.objects.get_or_create(
        journal_ID = ID,
        journal = title, #title,
        URL = j["j_url"], #j_url,
        image = j["img"], #img,
        publisher = j["pub"] #pub,
        )   


for (article, url) in zip(j["articles"], j["urls"]):
    Article.objects.get_or_create(
        article = article, 
        URL = url, 
        journal_ID = j["ID"], #ID,
        year = '2019', 
        month = 'May'
    )


    """
""" 
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







j = dict(HR,**Reli,**SHU_SYA,**SHUKYO,**CRR,**NU,**MTSR,**KaTetsu,**Tetsu,**CA,**PPR,**Nous,**PhilosCompass,**PhilosRev,**J_Appl_Philos,**Anthropol_Theory)

   
#

Journal.objects.get_or_create(
    journal_ID = j["ID"], #ID,
    journal = j["title"], #title,
    URL = j["j_url"], #j_url,
    image = j["img"], #img,
    publisher = j["pub"] #pub,
    )   


for (article, url) in zip(j["articles"], j["urls"]):
    Article.objects.get_or_create(
        article = article, 
        URL = url, 
        journal_ID = j["ID"], #ID,
        year = '2019', 
        month = 'May'
    )


context = {"ID":ID, "title":title, "j_url": j_url, "img":img, "pub":pub, "articles":articles, "urls":urls}

j =  Anthropol_Theory + KaTetsu + Tetsu + CA + PPR + Nous + J_Appl_Philos + PhilosCompass + PhilosRev + SHU_SYA + SHUKYO + CRR + Reli + NU + HR + MTSR
#dict(HR,**MTSR,**NU)
   

j=[]
j.append(KaTetsu)
j.append(Tetsu)
j.append(CA)
j.append(PPR)

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
    

#Journal.object.create(journal = HR_paper[0])
#paper_titles = HR_paper.list
#for paper_title in paper_titles:
 #   Article(article = paper_title).save
    


def paper_titles(request):
    HR = HR_chicago.HR_paper_titles()
    NU = Religion_brill.NU_paper_titles()
    Reli = Reli_routledge.Reli_paper_titles()
    MTSR = Religion_brill.MTSR()
    CRR = religion_sage.CRR()
    context = dict(HR,**NU,**Reli,**MTSR,**CRR)
    return render(request, "konchiwa.html", context)

    
"""   
