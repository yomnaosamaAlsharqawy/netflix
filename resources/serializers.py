from rest_framework import serializers
from resources.models import Movies

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id','name','description','time','image','year' ,'likes', 'dislikes' , 'url' , 'age' ,'views' ,'trailer']