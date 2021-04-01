from rest_framework import serializers

from resources.models import Casts, Genres, Moods, Tvshows, Seasons, Episodes


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


class SeasonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seasons
        fields = '__all__'


class TvshowsSerializer(serializers.ModelSerializer):
    moods = MoodsSerializer(read_only=True, many=True)
    seasons = SeasonsSerializer(read_only=True, many=True)

    class Meta:
        model = Tvshows
        fields = ['id', 'name', 'image', 'views', 'age', 'moods', 'seasons']


class TvshowsdetailedSerializer(serializers.ModelSerializer):
    moods = MoodsSerializer(read_only=True, many=True)
    seasons = SeasonsSerializer(read_only=True, many=True)
    genres = GenresSerializer(read_only=True, many=True)
    casts = CastSerializer(read_only=True, many=True)

    class Meta:
        model = Tvshows
        fields = "__all__"


class EpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodes
        fields = "__all__"
