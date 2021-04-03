from django.contrib.auth.models import User
from django.db import models
from accounts.submodels.plan import Plan
from django.contrib.auth.models import AbstractBaseUser
# from accounts.models import PaymentMethod

REGISTRATION_STEPS = [
    ('0', 'completed'),
    ('1', 'step1'),
    ('2', 'step2'),
    ('3', 'step3'),
]


class Account(AbstractBaseUser):
    USERNAME_FIELD = 'email'

    email = models.EmailField(unique=True, null=False, blank=False)
    plan_id = models.ForeignKey(Plan, on_delete=models.SET_NULL, related_name='users', null=True)
    # payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    registration_state = models.CharField(max_length=10, choices=REGISTRATION_STEPS, default=REGISTRATION_STEPS[1][0], null=False)

    def __str__(self):
        return self.email

    @property
    def profile(self):
        return self.profile_set.all()
