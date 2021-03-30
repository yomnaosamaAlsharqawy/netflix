from rest_framework import serializers
from resources.models import Movies,Casts

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id','name','description','time','image','year' ,'likes', 'dislikes' , 'url' , 'age' ,'views' ,'trailer']

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casts
        fields = ['id','name','role','movie','tv_show']
