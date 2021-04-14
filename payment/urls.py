from django.urls import path
from .views import create_payment

urlpatterns = [
    path('checkout/', create_payment),
]
