from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

from accounts.models import Profile
from resources.models import Movies, Tvshows
from django.contrib.contenttypes.fields import GenericForeignKey


class List(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, null=True, blank=True)
    tv_show = models.ForeignKey(Tvshows, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.profile.name
