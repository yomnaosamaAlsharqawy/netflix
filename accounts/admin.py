from django.contrib import admin
from accounts.models import Profile
from accounts.submodels.plan import Plan
from accounts.models import Account


# Register your models here.
admin.site.register(Account)
admin.site.register(Profile)
admin.site.register(Plan)
