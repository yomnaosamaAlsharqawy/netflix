from django.contrib.auth.models import User
from django.db import models
from . import Plan
# from . import PaymentMethod


class Account(User):
    email = models.EmailField(primary_key=True, unique=True, null=False, balnk=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    plan_id = models.ForeignKey(Plan, on_delete=models.SET_NULL, related_name='users')
    # payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    registration_state = models.CharField(choices=['step1', 'step2', 'step3', 'completed'], default='step1', null=False)

    def __str__(self):
        return self.email
