from rest_framework import serializers
from .models import Movies,Casts,Genres,Moods





class CastSerializer(serializers.ModelSerializer):
    class Meta():
        model = Casts
        fields = '__all__'

class GenresSerializer(serializers.ModelSerializer):
    class Meta():
        model = Genres
        fields = '__all__'

class MoodsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Moods
        fields = '__all__'
        

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = Movies
        #fields = ['name','description','time','image','year','likes','dislikes','url','age','views','trailer','casts','moods','genres']
        fields = '__all__'
        
    casts = CastSerializer(read_only=True, many=True)
    genres = GenresSerializer(read_only=True, many=True)
    moods = MoodsSerializer(read_only=True,many=True)



