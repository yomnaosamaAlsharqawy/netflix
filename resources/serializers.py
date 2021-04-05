from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from resources.models import Movies,Tvshows,Casts,Genres,Moods,Country
# from resources.models import Snippet

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#
#     def create(self, validated_data):
#         return Snippet(validated_data)
#
#
#     def update(self, instance, validated_data):
#
#         instance.title = validated_data.get('title',instance.title)
#         instance.code = validated_data.get('code',instance.code)
#         instance.linenos = validated_data.get('linenos',instance.linenos)
#         instance.save()
#         return instance

#
# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ['id', 'title', 'code', 'linenos']
#


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

    casts = CastSerializer(many=True,read_only=True)
    genres = GenresSerializer(many=True,read_only=True)
    moods = MoodsSerializer(many=True,read_only=True)
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Movies
        fields = '__all__'

class TvshowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tvshows
        fields = '__all__'

    casts = CastSerializer(read_only=True, many=True)
    genres = GenresSerializer(read_only=True, many=True)
    moods = MoodsSerializer(read_only=True, many=True)
    country = CountrySerializer(read_only=True)