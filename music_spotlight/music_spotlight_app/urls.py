from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('newartist/', views.newArtist, name='newArtist'),
    path('showartists/', views.showArtists, name='showArtists'),
    path('showalbums/', views.showAlbums, name='showAlbums'),
    path('newalbum/', views.newAlbum, name='newAlbum'),
]