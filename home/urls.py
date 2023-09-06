from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name="blog_list"),
    path('home', views.home, name="home"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('create/', views.create_blog_post, name='create'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('search/', views.search_results, name='search_results'),


]