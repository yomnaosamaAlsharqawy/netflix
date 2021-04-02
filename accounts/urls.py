from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("test/", views.test),

    # Account Endpoints
    path("check-email/", views.AccountCheck.as_view()),
    path("login/", obtain_auth_token),
    path("register/", views.AccountCreate.as_view()),
    path("<int:pk>/", views.AccountRetrieveUpdate.as_view()),

    # Profile Endpoints
    path("profiles/<int:pk>", views.ProfileList.as_view()),  # pk of parent account
    path("<int:pk>/profiles/new", views.ProfileCreate.as_view()),  # pk of parent account
    path("<int:pk>/profiles/", views.RetrieveUpdateDestroyAPIView.as_view()),  # pk of parent account

    # Plan Endpoints
    path("plans/", views.PlanList.as_view()),
]
