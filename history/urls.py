from django.urls import path

from history.views import HistoryController

urlpatterns=[
    path('', HistoryController.as_view()),
]