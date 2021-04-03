from django.db import models
from accounts.models.account import Account


class Profile(models.Model):
    name = models.CharField(max_length=50, default=f"Profile_{id}", null=False)
    pin_code = models.CharField(max_length=5, null=True, blank=True)
    image = models.ImageField(upload_to="accounts/profiles/images", null=True, blank=True)
    account_id = models.ForeignKey(Account, related_name='profiles', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(f"{self.account_id}_{self.name}")
