from django.urls import path
from .views import *

urlpatterns = [
    path('generator', HomePageGenerator.as_view()),
    path('popular', Popular.as_view()),

]
