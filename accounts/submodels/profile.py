from django.db import models
from accounts.models import Account


class ProfileImage(models.Model):
    name = models.CharField(max_length=20)
    image_url = models.URLField()

    def __str__(self):
        return str(self.name)


class Profile(models.Model):
    name = models.CharField(max_length=50, default=f"Profile_{id}", null=False)
    pin_code = models.CharField(max_length=5, null=True, blank=True)
    account_id = models.ForeignKey(Account, related_name='profiles', on_delete=models.SET_NULL, null=True, blank=True)
    image_id = models.ForeignKey(ProfileImage, on_delete=models.SET_NULL, related_name='profiles', null=True)

    def __str__(self):
        return str(f"{self.account_id}_{self.name}")

    def image_url(self):
        image_url = self.image_id.image_url
        return image_url
