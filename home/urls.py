from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # /
    path('',views.home,name='home'),
    # /about
    path('about',views.about,name='about'),
     # /contact
    path('contact',views.contact,name='contact'),
     # /search
    path('search',views.search,name='search'),
     # /signup
    path('signup',views.handleSignup, name='handleSignup'),
     # /login
    path('login',views.handleLogin, name='handleLogin'),
     # /logout
    path('logout',views.handleLogout, name='handleLogout'),
]
