from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # /blog
    path('',views.blogHome,name='blogHome'),
    # /blog/<Any string variable>
     path('<str:slug>',views.blogPost,name='blogPost'),

]
