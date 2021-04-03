from django.contrib import admin
from accounts.models.profile import Profile
from accounts.models.plan import Plan
from accounts.models.account import Account


# Register your models here.
admin.site.register(Account)
admin.site.register(Profile)
admin.site.register(Plan)
