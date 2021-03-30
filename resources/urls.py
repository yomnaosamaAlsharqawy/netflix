from django.urls import path

from resources import views

urlpatterns = [
    path("world", views.index, name="index"),
    path("movies", views.show_all_movies, name="movies"),
    path("create_movie",views.create_movie,name="create movie"),
    path("create_cast", views.create_cast, name="cast"),
    path("casts", views.show_all_casts, name="casts"),
]
