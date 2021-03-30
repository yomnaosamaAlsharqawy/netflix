from django.shortcuts import render
<<<<<<< HEAD
from django.http import response
from resources.models import Movies,Tvshows,Moods,Casts,Genre
from resources.serializers import MovieSerializer,CastSerializer
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


@api_view(["POST",])
def create_movie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "Movie has been created successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors,
    }, status=status.HTTP_400_BAD_REQUEST)




@api_view(["GET",])
def show_all_casts(request):
    casts = Casts.objects.all()
    serializer = CastSerializer(instance=casts,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(["POST",])
def create_cast(request):
    serializer = CastSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "Cast has been created successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors,
    }, status=status.HTTP_400_BAD_REQUEST)

=======

# Create your views here.
>>>>>>> master
