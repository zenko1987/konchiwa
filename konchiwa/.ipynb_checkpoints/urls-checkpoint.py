{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}

#Konchiwa

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from django.conf.urls import url
from django.contrib import admin
from konchiwa import views




app_name = 'konchiwa' #django2.0から必要になったnamespace定義
urlpatterns = [
    path('', views.paper_titles,name='paper_titles'),
    path('religion/', views.religion,name='religion'),
    path('cul_anthropology/', views.cul_anthropology, name='cul_anthropology'),
    path('history/', views.history,name='history'),
    path('linguistics/', views.linguistics,name='linguistics'),
    path('literature/', views.literature,name='literature'),
    path('pedagogy/', views.pedagogy,name='pedagogy'),
    path('psychology/', views.psychology,name='psychology'),
    path('archeology/', views.archeology,name='archeology'),
    path('philosophy/', views.philosophy,name='philosophy'),
    path('aca_writing/', views.aca_writing,name='aca_writing'),
    path('boards/<int:pk>/', views.TopicListView.as_view(), name='board_post'),# 掲示板　
    path('boards/<int:pk>/new/',views.new_topic, name='new_topic'),
    path('boards/<int:pk>/topics/<int:topic_pk>/', views.PostListView.as_view(), name='topic_posts'),#コメント
    path('boards/<int:pk>/topics/<int:topic_pk>/reply/', views.reply_topic, name='reply_topic'),#返信
    path('boards/<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
    #path('reply/', views.reply, name='reply'),#　reply
    path('home/', views.BoardListView.as_view(), name='home'),
    path('reset/',
    auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ),
    name='password_reset'),
path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    name='password_reset_confirm'),
path('reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
    name='password_reset_done'),
path('reset/complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
    name='password_reset_complete'),
path('settings/password/',auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
    name='password_change'),
path('settings/password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),
path('settings/account/',accounts_views.UserUpdateView.as_view(), name='my_account')
      
    
]

#as_view()は、汎用ビューを呼び出す際に使う書き方
