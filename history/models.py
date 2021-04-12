from django.db import models

from accounts.models import Profile
from resources.models import Movies, Tvshows


class History(models.Model):
    class Meta:
        verbose_name = "History"
        verbose_name_plural = "Histories"
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, null=True, blank=True)
    tv_show = models.ForeignKey(Tvshows, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.profile.name
