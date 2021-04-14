from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('episodes', EpisodeController.as_view()),
    path('oneepisode', OneEpisode.as_view()),
    path("movie", MovieController.as_view()),
    path("tv_show", TvShowsController.as_view()),
    path('moreinfo', MoreInfo.as_view()),
    path('suggestion', Suggestion.as_view()),
    path('season', SeasonController.as_view()),
    path("top_ten_movies/<str:country>", views.top_ten_movies, name="top_ten_movies"),
    path("top_ten_tv_show/<str:country>", views.top_ten_tv_show, name="top_ten_tv_show"),
    path("filters", Filters.as_view()),
    path("likes", Likes.as_view()),
    path("views", Views.as_view()),
    path("search", Search.as_view()),
    path("genres", views.show_all_genres),
    path("create_cast", views.create_cast, name="cast"),
    path("casts", views.show_all_casts, name="casts"),
    path("add_country", views.add_country, name="add_country"),
    path("get_country", views.show_all_countries, name="show_country"),

]
