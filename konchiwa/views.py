from django.shortcuts import render
from django.shortcuts import redirect
from . import models
#ページ送り
from pure_pagination.mixins import PaginationMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template import Context, loader
#モデル
from .models import Journal
from .models import Article
#掲示板
from .models import Post
from .models import Board
from .models import Topic
#from .models import Person
from django.shortcuts import render, redirect #コメント保存用
from django.http import Http404





def paper_titles(request):
    context = {
        'journals': Journal.objects.all(), 
        'articles': Article.objects.all(),
        'comments': Post.objects.all(),
        'boards': Board.objects.all(),        
    }
    return render(request, "konchiwa.html", context)


def philosophy(request):
    context = {
        'journals': Journal.objects.all(), 
        'articles': Article.objects.all(),
        'comments': Post.objects.all(),
        'board': Board.objects.all(), 
    }
    return render(request, "philosophy.html", context)


def religion(request):
    context = {
        'journals': Journal.objects.all(), 
        'articles': Article.objects.all(),
        'comments': Post.objects.all(),
        'board': Board.objects.all(),
    }
    return render(request, "religion.html", context)


def cul_anthropology(request):
    context = {
        'journals': Journal.objects.all(), 
        'articles': Article.objects.all(),
        'comments': Post.objects.all(),
        'board': Board.objects.all(),
    }
    return render(request, "cul_anthropology.html", context)


def history(request):
    context = {
        'journals': Journal.objects.all(), 
        'articles': Article.objects.all(),
        'comments': Post.objects.all(),
        'board': Board.objects.all(),
    }
    return render(request, "history.html", context)


def linguistics(request):
    context = {
        'journals': Journal.objects.all(), 
        'articles': Article.objects.all(),
        'comments': Post.objects.all(),
        'board': Board.objects.all(),    
    }
    return render(request, "linguistics.html", context)


def pedagogy(request):
    context = {
        'journals': Journal.objects.all(), 
        'articles': Article.objects.all(),
        'comments': Post.objects.all(),
        'board': Board.objects.all(),
    }
    return render(request, "pedagogy.html", context)


def psychology(request):
    context = {
        'journals': Journal.objects.all(), 
        'articles': Article.objects.all(),
        'comments': Post.objects.all(),
        'board': Board.objects.all(),
    }
    return render(request, "psychology.html", context)


def archeology(request):
    context = {
        'journals': Journal.objects.all(), 
        'articles': Article.objects.all(),
        'comments': Post.objects.all(),
        'board': Board.objects.all(),   
    }
    return render(request, "archeology.html", context)


def literature(request):
    context = {
        'journals': Journal.objects.all(), 
        'articles': Article.objects.all(),
        'comments': Post.objects.all(),
        'board': Board.objects.all(),   
    }
    return render(request, "literature.html", context)

def aca_writing(request):
    context = {
        'journals': Journal.objects.all(), 
        'articles': Article.objects.all(),
        'comments': Post.objects.all(),
        'board': Board.objects.all(),  
    }
    return render(request, "aca_writing.html", context)

"""
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})
"""




#------------掲示板-----------------
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import NewTopicForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.db.models import Count
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy


#------------掲示板-----------------

class BoardListView(ListView):
    model = Board #model = Boardとすることで、今回の例だとBoard.objects.all()を裏側で行う。queryset = Board.objects.all()と同じ
    context_object_name = 'boards' #データベースから取り出した一覧データを、templateに渡す。何もないと <model name>_listになる
    template_name = 'home.html'#どのテンプレートを使うかの指定 指定しなければ　<app name>/<model name>_list.html

    

#board_post
class TopicListView(ListView):
    model = Topic
    context_object_name = 'topics'
    template_name = 'board.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        kwargs['board'] = self.board
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.board = get_object_or_404(Board, pk=self.kwargs.get('pk'))
        queryset = self.board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
        return queryset   
    

#topic_posts
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'topic_posts.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        
        session_key = 'viewed_topic_{}'.format(self.topic.pk)
        if not self.request.session.get(session_key, False):
            self.topic.views += 1
            self.topic.save()
            self.request.session[session_key] = True
            
        kwargs['topic'] = self.topic
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.topic = get_object_or_404(Topic, board__pk=self.kwargs.get('pk'), pk=self.kwargs.get('topic_pk'))
        queryset = self.topic.posts.order_by('created_at')
        return queryset    
    
    
   
@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
            return redirect('konchiwa:topic_posts', pk=pk, topic_pk=topic.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})
    
    
    
#返信
@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            
            topic.last_updated = timezone.now()
            topic.save() 
            
            return redirect('konchiwa:topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})



#edit_post
@method_decorator(login_required, name='dispatch')    
class PostUpdateView(UpdateView): 
    model = Post
    fields = ('message', )
    template_name = 'edit_post.html'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)
    
    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('konchiwa:topic_posts', pk=post.topic.board.pk, topic_pk=post.topic.pk)

    
#クラスを@login_requiredデコレータで直接装飾することはできない。@method_decoratorでどのメソッドを装飾するか命令。dispatchを使うのが一般的
    
    

    


"""  
    
    
#board_post
class TopicListView(ListView):
    model = Topic
    context_object_name = 'topics'
    template_name = 'topics.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        kwargs['boards'] = self.board
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.board = get_object_or_404(Board, pk=self.kwargs.get('pk'))
        queryset = self.board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
        return queryset   
    


        
        
        
    
   
def board_post(request, pk):
    boards = get_object_or_404(Board, pk=pk)
    topics = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
    return render(request, 'topics.html', {'boards': boards, 'topics': topics})
 

#コメントの登録
def topic_posts(request, pk, topic_pk):
    topics = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    topics.views += 1
    topics.save()
    return render(request, 'topic_posts.html', {'topics': topics})
    
    
    
    #page
from django.core.paginator import Paginator
paginator = Paginator(queryset, 2)#ページ内掲載数
    
    
   @require_POST
def reply(request):
    if request.method == "POST":
        reply = get_object_or_404(Comment, id=comment_id)
        form = ReplyForm(request.POST, request.FILES, instance=reply)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.reply = form.reply
            comment.save()
            return redirect('konchiwa:new_comment', id=id, title_id=title_id)
    else:
        form = ReplyForm
        return render(request, 'konchiwa.html', {'form': form })
 
      
    
    
    
 , id=id, title=Comment.title   
    
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    form = CommentForm
    return render(request, 'konchiwa.html', {'form': form, 'comment':comment })
    
    
    
def new_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('konchiwa:paper_titles')
    else:
#        form = CommentForm
        return render(request, 'konchiwa.html', {'form': form })


def new_file(request):
    if request.method == 'GET':
        return render(request, 'konchiwa/konchiwa.html', {
            'form': FileForm(),
        })    
    
    elif request.method == 'POST':                                                     
        form = FileForm(request.POST, request.FILES)
        if not form.is_valid():
            raise ValueError('invalid form')

        file = Comment()
        attachment.image = form.cleaned_data['image']
        attachment.file = form.cleaned_data['file']
        attachment.save()

        return redirect('/')    
    
    
    
    
#コメントの削除
@require_POST
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('konchiwa:paper_titles')


def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    form = CommentForm
    return render(request, 'konchiwa.html', {'form': form, 'comment':comment })




  


#雑誌
from konchiwa.journals import HR_chicago
from konchiwa.journals import Religion_brill
from konchiwa.journals import Reli_routledge
from konchiwa.journals import religion_sage

konchiwa:new_comment






#History of religions,Numen
def paper_titles(request):
    HR = HR_chicago.HR_paper_titles()
    NU = Religion_brill.NU_paper_titles()
    Reli = Reli_routledge.Reli_paper_titles()
    MTSR = Religion_brill.MTSR()
    CRR = religion_sage.CRR()
    context = dict(HR,**NU,**Reli,**MTSR,**CRR)
    return render(request, "konchiwa.html", context)





#上記モデルの取り込み
import requests
from bs4 import BeautifulSoup
import lxml
import re

from konchiwa.models import Journal
from konchiwa.models import Article

#NU = Religion_brill.NU_paper_titles()
#Reli = Reli_routledge.Reli_paper_titles()
#MTSR = Religion_brill.MTSR()
#CRR = religion_sage.CRR()
#context = dict(HR,**NU,**Reli,**MTSR,**CRR)


 <tr>
          <td>
            <a href="{% url 'konchiwa:board_post' board.pk %}">{{ board.board }}</a>
            <small class="text-muted d-block">{{ comment.comment }}</small>
          </td>
          <td class="align-middle">0</td>
          <td class="align-middle">0</td>
          <td></td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
    

"""
    
            

                                                                                                                                                                           
                                                                                                                                                                            

            