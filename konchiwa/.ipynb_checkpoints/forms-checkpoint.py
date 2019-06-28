from django.forms import ModelForm
from .models import Post
from .models import Topic
from django import forms   


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Write a seed of arguments'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )
    #attachment = forms.FileField()

    class Meta:
        model = Topic
        fields = ['subject', 'message']
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]
      

        
""" 
class FileForm(forms.Form):

    image = forms.ImageField()
    file = forms.FileField()
    
    
       
         comment_ID = models.IntegerField(blank=True, null=True)
    board_ID = models.IntegerField(blank=True, null=True)
    person_ID = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=128, editable=True, blank=True, null=True)
    post = models.TextField(blank=True, null=True)
    comment_div = models.IntegerField(blank=True, null=True)
    good = models.IntegerField(blank=True, null=True)
    reply = models.IntegerField(blank=True, null=True)
    attachment = models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add = True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add = True,blank=True, null=True)
    
    
    
    

        """    