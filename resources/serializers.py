from rest_framework import serializers
from .models import Movies

class MovieSerializer(serializers.ModelSerializer):
    class Meta():
        model = Movies
        #fields = ['name','description','time','image','year','likes','dislikes','url','age','views','trailer','casts','moods','genres']
        fields = '__all__'



