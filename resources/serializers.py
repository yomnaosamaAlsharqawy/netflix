from rest_framework import serializers
from resources.models import Movies,Tvshows,Casts,Genres,Moods,Country


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casts
        fields = ['name','role']


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['name']


class MoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moods
        fields = ['name']



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']



class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

    casts = CastSerializer(read_only=True, many=True)
    genres = GenresSerializer(read_only=True, many=True)
    moods = MoodsSerializer(read_only=True, many=True)
    country = CountrySerializer(read_only=True)



class TvshowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tvshows
        fields = '__all__'

    casts = CastSerializer(read_only=True, many=True)
    genres = GenresSerializer(read_only=True, many=True)
    moods = MoodsSerializer(read_only=True, many=True)
    country = CountrySerializer(read_only=True)