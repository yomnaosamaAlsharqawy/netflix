from rest_framework import serializers
from .models import *


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casts
        fields = '__all__'


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'


class MoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moods
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    moods = MoodsSerializer(read_only=True, many=True)

    class Meta:
        model = Movies
        fields = ['id', 'name', 'type', 'image', 'trailer', 'views', 'age', 'time', 'moods', 'description', 'year']


class MovieInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

    casts = CastSerializer(read_only=True, many=True)
    genres = GenresSerializer(read_only=True, many=True)
    moods = MoodsSerializer(read_only=True, many=True)
    country = CountrySerializer(read_only=True)


class SeasonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seasons
        fields = '__all__'


class TvshowsSerializer(serializers.ModelSerializer):
    moods = MoodsSerializer(read_only=True, many=True)
    seasons = SeasonsSerializer(read_only=True, many=True)

    class Meta:
        model = Tvshows
        fields = ['id', 'name', 'trailer', 'type', 'image', 'views', 'age', 'moods', 'seasons', 'description', 'year']


class TvshowsdetailedSerializer(serializers.ModelSerializer):
    moods = MoodsSerializer(read_only=True, many=True)
    seasons = SeasonsSerializer(read_only=True, many=True)
    genres = GenresSerializer(read_only=True, many=True)
    casts = CastSerializer(read_only=True, many=True)
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Tvshows
        fields = "__all__"


class EpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodes
        fields = "__all__"
