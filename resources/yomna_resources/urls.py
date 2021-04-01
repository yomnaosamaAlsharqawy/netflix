from django.urls import path

from resources.yomna_resources.views import tvshowdetail

urlpatterns = [
    path('tvshowdetail/<int:index>', tvshowdetail, name='index'),
]
