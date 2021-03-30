from django.shortcuts import render
from rest_framework.response import Response
from .models import Movies
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
#from rest_framework.permissions import IsAuthenticated
#from rest_framework import generics
from .serializers import MovieSerializer


@api_view(["GET",])
def index(request):
    movies = Movies.objects.all()
    serializer = MovieSerializer(instance=movies,many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)



