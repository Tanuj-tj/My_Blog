from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    # /blog/postComment
    path('postComment',views.postComment,name='postComment'),

    # /blog
    path('',views.blogHome,name='blogHome'),

    # /blog/<Any string variable>
    path('<str:slug>',views.blogPost,name='blogPost'),


     # /blog/edit
    path('<str:slug>/blogEdit',views.blogEdit,name='blogEdit'),
]