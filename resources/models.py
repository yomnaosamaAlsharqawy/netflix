from django.db import models


class Casts(models.Model):
    name = models.CharField(max_length=25)
    role = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Moods(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name

class Movies(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=200)
    time = models.TimeField()
    image = models.ImageField(upload_to='movies/posters')
    year = models.DateField()
    likes = models.IntegerField(null=True)
    dislikes = models.IntegerField(null=True)
    url = models.URLField()
    age = models.IntegerField()
    views = models.IntegerField(null=True)
    trailer = models.URLField()
    casts = models.ManyToManyField(Casts,related_name="cast")
    genres = models.ManyToManyField(Moods)
    moods = models.ManyToManyField(Genres)
    country = models.ForeignKey(Country , on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name


class Tvshows(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=200)
    time = models.TimeField()
    image = models.ImageField(upload_to='movies/posters')
    year = models.DateField()
    likes = models.IntegerField(null=True)
    dislikes = models.IntegerField(null=True)
    age = models.IntegerField()
    views = models.IntegerField(null=True)
    trailer = models.URLField()
    casts = models.ManyToManyField(Casts)
    moods = models.ManyToManyField(Moods)
    genres = models.ManyToManyField(Genres)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

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
    url = models.URLField()
    season = models.ForeignKey(Seasons,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name