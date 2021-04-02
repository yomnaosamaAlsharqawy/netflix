from django.db import models
from . import Account


class Profile(models.Model):
    name = models.CharField(max_length=50, default=f"Profile_{id}")
    pin_code = models.CharField(max_length=5)
    image = models.ImageField(upload_to="/")
    account_id = models.ForeignKey(Account, related_name='profiles', on_delete=models.SET_NULL())

    def __str__(self):
        return str(f"{self.account_id}_{self.name}")
