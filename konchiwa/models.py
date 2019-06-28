from markdown import markdown
from django.db import models
import uuid
from bulk_update.helper import bulk_update
from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilter
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.utils.html import mark_safe
import math


class Journal(models.Model):
    journal_ID = models.CharField(max_length=128)
    journal = models.CharField(max_length=128, editable=True)
    number = models.CharField(max_length=128, blank=True, null=True)
    URL = models.URLField(blank=True, null=True)
    publisher = models.CharField(max_length=128, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='document/%Y/%m/%d')
    discipline = models.CharField(max_length=128, editable=True, blank=True, null=True)
    
    def __str__(self):
        return self.journal
    

class Article(models.Model):
    journal_ID = models.CharField(max_length=128)
    journal = models.CharField(max_length=128, editable=True, blank=True, null=True)
    article = models.CharField(max_length=128, editable=True, blank=True, null=True)
    date = models.DateField(auto_now_add = True)
    URL = models.URLField(blank=True, null=True)
    author = models.CharField(max_length=128, editable=True, blank=True, null=True)
    discipline = models.CharField(max_length=128, editable=True, blank=True, null=True)
    
    def __str__(self):
        return self.article
    
        
        
        
class Author(models.Model):
    author_ID = models.IntegerField()
    fitst = models.CharField(max_length=128, editable=True, blank=True, null=True)
    last = models.CharField(max_length=128, editable=True, blank=True, null=True)
    area = models.CharField(max_length=128, editable=True, blank=True, null=True)

    def __str__(self):
        return self.fitst 
    


class Discipline(models.Model):
    discipline_ID = models.IntegerField(blank=True, null=True)
    discipline = models.CharField(max_length=128, editable=True)
    
    def __str__(self):
        return self.discipline
    
    
class Publisher(models.Model):
    publisher = models.CharField(max_length=128, editable=True, blank=True, null=True)
    
    def __str__(self):
        return self.publisher
   

class Board(models.Model):
    name = models.CharField(max_length=128, unique=True, editable=True, blank=True, null=True)
    discipline = models.CharField(max_length=128, editable=True)
    description = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()
    
    
class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')
    last_updated = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)#何人見たかをカウントするもの

    def __str__(self):
        return self.subject

    def get_page_count(self):
        count = self.posts.count()
        pages = count / 20
        return math.ceil(pages)

    def has_many_pages(self, count=None):
        if count is None:
            count = self.get_page_count()
        return count > 6

    def get_page_range(self):
        count = self.get_page_count()
        if self.has_many_pages(count):
            return range(1, 5)
        return range(1, count + 1)
    
    def get_last_ten_posts(self):
            return self.posts.order_by('-created_at')[:10]
    
     

    
class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    attachment = models.FileField(upload_to='documents/%Y/%m/%d', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))
    
    
    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)
    

    


"""   

class Board(models.Model):
    board_ID = models.IntegerField(blank=True, null=True)
    board = models.CharField(max_length=128, editable=True, blank=True, null=True)
    discipline = models.CharField(max_length=128, editable=True)
    post = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.discipline

    
class Comment(models.Model):
    comment_ID = models.IntegerField(blank=True, null=True)
    board_ID = models.IntegerField(blank=True, null=True)
    person_ID = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=128, editable=True, blank=True, null=True)
    reply = models.TextField(blank=True, null=True)
    comment_div = models.IntegerField(blank=True, null=True)
    good = models.IntegerField(blank=True, null=True)
    attachment = models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add = True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add = True,blank=True, null=True)
    #reply_number = models.IntegerField(blank=True, null=True)
    
    class Meta:
        # sort comments in chronological order by default
        ordering = ('created_at',)
        

class Person(models.Model):
    person_ID = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    fitst = models.CharField(max_length=128, editable=True, blank=True, null=True)
    last = models.CharField(max_length=128, editable=True, blank=True, null=True)
    E_mail = models.IntegerField(blank=True, null=True)
    my_site = models.URLField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    registered_at = models.DateTimeField(auto_now_add = True,blank=True, null=True)
    country = models.CharField(max_length=128, editable=True, blank=True, null=True)
    
    def __str__(self):
        return self.first
"""   

#"""   
#上記モデルの取り込み    
from konchiwa.models import Journal
from konchiwa.models import Article

#宗教 
from konchiwa.journals.religion import HR_chicago #ファイル名
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

#"""
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

#"""


#文化人類学
from konchiwa.journals.cul_anthropology import CA
from konchiwa.journals.cul_anthropology import CA_sage
from konchiwa.journals.cul_anthropology import JA_anth
from konchiwa.journals.cul_anthropology import annurev_anthro

CA = CA.CA()
Anthropol_Theory = CA_sage.Anthropol_Theory()
Bunka_jinrui = JA_anth.Bunka_jinrui()
annurev_anthro = annurev_anthro.annurev_anthro()

# CAとった
b = [CA, HR, Reli, SHU_SYA, SHUKYO, CRR, NU, MTSR, Anthropol_Theory, Bunka_jinrui, annurev_anthro, KaTetsu, Tetsu, PPR, Nous, PhilosCompass, J_Appl_Philos]#PhilosRev,


for j in b:
    Journal.objects.get_or_create(
        journal_ID = j['ID'],
        journal = j['title'],
        URL = j['j_url'],
        image = j["img"], 
        publisher = j["pub"],
        discipline = j["discipline"]
        )   



    for article, url, author in zip(j["articles"], j["urls"], j["authors"]):
        Article.objects.get_or_create(
            article = article,
            journal_ID = j["ID"], #ID,
            journal = j['title'],
            URL = url, 
            discipline = j["discipline"],
            author = author
            )    


#"""        
    
"""
        URL = j_url,
        image = image,
        publisher = publisher
    )


"""







"""    
#-------------all_journals.py----------------

from . import all_journals

ID = all_journals.ID()
title = all_journals.title()
j_url = all_journals.j_url()
image = all_journals.image()
publisher = all_journals.publisher()
article = all_journals.article()
url = all_journals.url()



    Journal.objects.update_or_create(journal_ID = ID)
#-------------雑誌の登録----------------


Journal.objects.get_or_create(
    for ID in IDs:
        journal_ID = ID,
        journal = title,
        URL = j_url,
        image = image,
        publisher = publisher
        discipline = discipline
    )
"""

"""
#-------------論文の登録----------------

Article.objects.get_or_create(
        article = article, 
        URL = url, 
        journal_ID = ID,
        year = '2019', 
        month = 'May'
        discipline = discipline
    )
    
"""