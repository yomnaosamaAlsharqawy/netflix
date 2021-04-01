from django.shortcuts import render
from rest_framework.response import Response
from .models import Movies , Tvshows
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
#from rest_framework.permissions import IsAuthenticated
#from rest_framework import generics
from .serializers import MovieSerializer
from .yomna_resources.serializers import TvshowsSerializer

@api_view(['GET',])
def GetMovieWithGenres(request,genre):
    movies = Movies.objects.filter(genres__genre=genre)
    serializer = MovieSerializer(instance=movies,many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)


@api_view(['GET',])
def GetTvshowWithGenres(request,genre):
    tvshows = Tvshows.objects.filter(genres__genre=genre)
    serializer = TvshowsSerializer(instance=tvshows,many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK) 
    



