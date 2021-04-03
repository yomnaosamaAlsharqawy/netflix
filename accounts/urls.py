from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from accounts.views import account, profile, plan

urlpatterns = [
    # Account Endpoints
    path("check-email/", account.email_check),
    path("login/", obtain_auth_token),
    path("register/", account.AccountCreate.as_view()),
    path("<int:pk>/", account.AccountRetrieveUpdate.as_view()),

    # Profile Endpoints
    path("profiles/<int:pk>", profile.ProfileList.as_view()),  # pk of parent account
    path("<int:pk>/profiles/new", profile.ProfileCreate.as_view()),  # pk of parent account
    path("<int:pk>/profiles/", profile.RetrieveUpdateDestroyAPIView.as_view()),  # pk of parent account
    path("profiles/login/<int:pk>", profile.profile_login),

    # Plan Endpoints
    path("plans/", plan.PlanList.as_view()),
]
