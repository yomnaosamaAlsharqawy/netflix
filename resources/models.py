from django.db import models


# Create your models here.
class Casts(models.Model):
    name = models.CharField(max_length=25)
    role = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Genres(models.Model):
    genre = models.CharField(max_length=25)

    def __str__(self):
        return self.genre


class Moods(models.Model):
    mood = models.CharField(max_length=25)

    def __str__(self):
        return self.mood


class Movies(models.Model):
    name = models.CharField(max_length=25)
    # slug = models.SlugField(default=None, blank=True, unique=True, max_length=150)
    description = models.TextField(max_length=200)
    time = models.TimeField()
    image = models.ImageField()
    year = models.DateField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    url = models.FileField()
    age = models.IntegerField()
    views = models.IntegerField(default=0)
    trailer = models.FileField()
    casts = models.ManyToManyField(Casts)
    moods = models.ManyToManyField(Moods)
    genres = models.ManyToManyField(Genres)

    def __str__(self):
        return self.name


class Tvshows(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=200)
    image = models.ImageField()
    year = models.DateField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    age = models.IntegerField()
    views = models.IntegerField(default=0)
    trailer = models.FileField()
    casts = models.ManyToManyField(Casts)
    moods = models.ManyToManyField(Moods)
    genres = models.ManyToManyField(Genres)

    def __str__(self):
        return self.name

    @property
    def seasons(self):
        return self.seasons_set.all()


class Seasons(models.Model):
    season = models.IntegerField()
    tv_show = models.ForeignKey(Tvshows, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.tv_show.name + str(self.season)
    def __int__(self):
        return self.season

    @property
    def episodes(self):
        return self.episodes_set.all()


class Episodes(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    time = models.TimeField()
    image = models.ImageField()
    descriptions = models.TextField(max_length=200)
    url = models.FileField()
    season = models.ForeignKey(Seasons, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
