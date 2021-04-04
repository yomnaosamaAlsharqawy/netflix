from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views
from .views import *

urlpatterns = [
    path('get_country_movies/<str:c>', views.show_country_movies, name="show_country_movies"),
    path('getepisodes/<int:index>', ListEpisodes.as_view()),
    path('genresfilter/<str:type>/<str:genre>', ListByGenres.as_view()),
    path("movie", MovieController.as_view(), name="create movie"),
    path("tv_show", TvShowsController.as_view(), name="create tv show"),
    path("create_cast", views.create_cast, name="cast"),
    path("casts", views.show_all_casts, name="casts"),
    path("add_country", views.add_country, name="add_country"),
    path("get_country", views.show_all_countries, name="show_country"),
    path("top_ten_movies/<str:country>", views.top_ten_movies, name="top_ten_movies"),
    path("top_ten_tv_show/<str:country>", views.top_ten_tv_show, name="top_ten_tv_show"),
    path('moodsfilter/<str:type>/<str:mood>', ListByMoods.as_view()),
    path('castsfilter/<str:type>/<str:cast>', ListByCasts.as_view()),
    path('recentlyadded/<str:type>', RecentlyAdded.as_view()),
]
