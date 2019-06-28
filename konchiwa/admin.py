from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilter
from dal import autocomplete


# Register your models here.
#from .models import Religion
#from .models import Philosophy
#from .models import year
#from .models import month
#from .models import realm 
from .models import Journal
from .models import Article
from .models import Author
from .models import Discipline
from .models import Publisher


#admin.site.register(Religion)
#admin.site.register(Philosophy)
#admin.site.register(year)
#admin.site.register(month)
#admin.site.register(realm)
admin.site.register(Journal)
#admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Discipline)
admin.site.register(Publisher)



from .models import Post
from .models import Topic
from .models import Board

admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(Board)


#"""

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['journal_ID','journal','discipline'] 
    list_filter =  ['journal_ID','journal','discipline','date'] 
    date_hierarchy = 'date'



#admin.site.unregister(Article)    
admin.site.register(Article, ArticleAdmin)


#"""
"""

class ArticleFilter(AutocompleteFilter):
    title = 'Article' # display title
    field_name = 'articles' # name of the foreign key field
    
class JournalAdmin(admin.ModelAdmin):
    list_filter = [Article]
   
    
  
from .models import ArticleAdmin
from .models import JournalAdmin
from .models import ArticleFilter  
    
admin.site.register(JournalAdmin)
admin.site.register(ArticleFilter)    
    
    
"""