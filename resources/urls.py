from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    path('moviegenres/<str:genre>', views.GetMovieWithGenres),
    path('tvshowgenres/<str:genre>', views.GetTvshowWithGenres),
    path('getepisodes/<int:id>', views.GetEpisodes),
    
]