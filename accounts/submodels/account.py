from django.contrib.auth.models import User
from django.db import models
from accounts.submodels.plan import Plan

REGISTRATION_STEPS = [
    (1, 'step1'),
    (2, 'step2'),
    (3, 'step3'),
    (4, 'completed'),
]


class Account(User):
    plan_id = models.ForeignKey(Plan, on_delete=models.SET_NULL, related_name='users', null=True)
    country_code = models.CharField(max_length=2, null=True, blank=False)
    phone_number = models.CharField(max_length=25, null=True, blank=False)
    registration_state = models.IntegerField(choices=REGISTRATION_STEPS, default=REGISTRATION_STEPS[0][0], null=False)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username
