from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    # Account Endpoints
    path("check-email/", views.email_check),
    path("login/", obtain_auth_token),
    path("register/", views.AccountCreate.as_view()),
    path("<int:pk>/", views.AccountRetrieveUpdate.as_view()),

    # Profile Endpoints
    path("<int:account_id>/profiles/", views.ProfileList.as_view()),  # pk of parent account
    path("profiles/new/", views.ProfileCreate.as_view()),  # pk of parent account
    path("profiles/<int:pk>/", views.ProfileRetrieveUpdateDestroy.as_view()),  # pk of parent account
    path("profiles/<int:pk>/login/", views.profile_login),

    # Plan Endpoints
    path("plans/", views.PlanList.as_view()),
]
