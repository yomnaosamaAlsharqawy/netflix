from django.urls import path

from mylist.views import ListController

urlpatterns = [
    path('', ListController.as_view()),
]
