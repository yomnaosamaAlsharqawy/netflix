from django.urls import path

from resources import views

urlpatterns = [

    path("world", views.index, name="index"),
    path("movies", views.show_all_movies, name="movies"),
    path("tvshows", views.show_all_tv_shows, name="tv_shows"),
    path("create_movie",views.create_movie,name="create movie"),
    path("create_tv_show",views.create_tv_show,name="create tv show"),
    path("create_cast", views.create_cast, name="cast"),
    path("casts", views.show_all_casts, name="casts"),
    path("add_country", views.add_country, name="add_country"),
    path("get_country", views.show_all_countries, name="show_country"),
    path("get_country_movies/<str:country>", views.show_country_movies, name="show_country_movies"),
    path("top_ten_movies/<str:country>", views.top_ten_movies, name="top_ten_movies"),
    path("top_ten_tv_show/<str:country>", views.top_ten_tv_show, name="top_ten_tv_show"),

]
