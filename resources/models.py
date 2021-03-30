from django.db import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    time = models.TimeField()
    image = models.ImageField()
    year = models.DateField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    url  = models.URLField()
    age = models.IntegerField()
    views = models.IntegerField()
    trailer = models.URLField()

    def __str__(self):
        return self.name

class Tvshows(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    time = models.TimeField()
    image = models.ImageField()
    year = models.DateField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    age = models.IntegerField()
    views = models.IntegerField()
    trailer = models.URLField()

    def __str__(self):
        return self.name

class Seasons(models.Model):
    season = models.IntegerField()
    tv_show = models.ForeignKey(Tvshows,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.season

class Episodes(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    time = models.TimeField()
    image = models.ImageField()
    description = models.TextField()
    url = models.URLField()
    season = models.ForeignKey(Seasons,on_delete=models.SET_NULL,null=True)

    def __init__(self):
        return self.name
class Casts(models.Model):
    name = models.CharField(max_length=25)
    role = models.CharField(max_length=25)
    movie = models.ManyToManyField(Movies)
    tv_show = models.ManyToManyField(Tvshows)

    def __init__(self):
        return self.name

class Genre(models.Model):
    genre = models.CharField(max_length=25)
    movie = models.ManyToManyField(Movies)
    tv_show = models.ManyToManyField(Tvshows)

    def __init__(self):
        return self.genre

class Moods(models.Model):
    mood = models.CharField(max_length=25)
    movie = models.ManyToManyField(Movies)
    tv_show = models.ManyToManyField(Tvshows)

    def __init__(self):
        return self.mood
