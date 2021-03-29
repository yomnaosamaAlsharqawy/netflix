from django.urls import path

from resources import views

urlpatterns = [
    path("world", views.index, name="index"),
]
