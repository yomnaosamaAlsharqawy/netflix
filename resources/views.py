from django.shortcuts import render
from django.http import response
from resources.models import Movies,Tvshows,Moods,Casts,Genre
from resources.serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from rest_framework import status

def index(request):
     return response.HttpResponse("<h1>hello</h1>")

@api_view(["GET",])
def show_all_movies(request):
    movies = Movies.objects.all()
    serializer = MovieSerializer(instance=movies,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
