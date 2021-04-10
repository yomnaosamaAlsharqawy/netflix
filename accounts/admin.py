from django.contrib import admin
from accounts.submodels.plan import Plan
from accounts.models import Account, Profile, ProfileImage


# Register your models here.
admin.site.register(Account)
admin.site.register(Profile)
admin.site.register(ProfileImage)
admin.site.register(Plan)
