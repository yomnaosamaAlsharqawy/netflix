from django.db import models


class Casts(models.Model):
    class Meta:
        verbose_name = "Cast"
        verbose_name_plural = "Casts"

    name = models.CharField(max_length=25)
    role = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Genres(models.Model):
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    genre = models.CharField(max_length=25)

    def __str__(self):
        return self.genre


class Moods(models.Model):
    class Meta:
        verbose_name = "Mood"
        verbose_name_plural = "Moods"

    mood = models.CharField(max_length=25)

    def __str__(self):
        return self.mood


class Country(models.Model):
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    @property
    def movies(self):
        return self.movies_set.all()


class Movies(models.Model):
    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    name = models.CharField(max_length=25)
    description = models.TextField(max_length=200)
    type = models.CharField(default='movie', max_length=20)
    time = models.CharField(max_length=20)
    image = models.URLField()
    year = models.DateField()
    likes = models.IntegerField(default=0)
    url = models.URLField()
    age = models.IntegerField()
    views = models.IntegerField(default=0)
    trailer = models.URLField()
    casts = models.ManyToManyField(Casts)
    moods = models.ManyToManyField(Moods)
    genres = models.ManyToManyField(Genres)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Tvshows(models.Model):
    class Meta:
        verbose_name = "Tvshow"
        verbose_name_plural = "Tvshows"

    name = models.CharField(max_length=25)
    description = models.TextField(max_length=200)
    type = models.CharField(default='tv_show', max_length=20)
    image = models.URLField()
    year = models.DateField()
    likes = models.IntegerField(default=0)
    age = models.IntegerField()
    views = models.IntegerField(default=0)
    trailer = models.URLField()
    casts = models.ManyToManyField(Casts)
    moods = models.ManyToManyField(Moods)
    genres = models.ManyToManyField(Genres)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    @property
    def seasons(self):
        return self.seasons_set.all()


class Seasons(models.Model):
    class Meta:
        verbose_name = "Season"
        verbose_name_plural = "Seasons"

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
    class Meta:
        verbose_name = "Episode"
        verbose_name_plural = "Episodes"

    name = models.CharField(max_length=25)
    description = models.TextField(max_length=200)
    time = models.CharField(max_length=20)
    image = models.URLField()
    url = models.URLField()
    season = models.ForeignKey(Seasons, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.season.tv_show.name +" - "+ self.name + str(self.season.season)
