import json

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes

from resources.models import Tvshows, Casts, Moods, Genres, Movies
from resources.serializers import MovieSerializer


class MovieController(APIView, ):
    def get(self, request, *args, **kwargs):
        try:
            movies = Movies.objects.all()
            serializer = MovieSerializer(instance=movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            moods = json.loads(data['moods'])
            genres = json.loads(data['genres'])
            movie = Movies(name=data['name'], description=data['description'], year=data['year'], age=data['age'],
                           image=data['image'], trailer=data['trailer'], time=data['time'], url=data['url'])
            movie.clean()
            movie.save()
            cast_data = json.loads(data['casts'])
            for i in cast_data:
                cast = Casts.objects.create(name=i['name'], role=i['role'])
                movie.casts.add(cast)
            for i in moods:
                mood = Moods.objects.get(mood=i)
                movie.moods.add(mood)
            for i in genres:
                genre = Genres.objects.get(genre=i)
                movie.genres.add(genre)

            return Response(data={
                "success": True,
                "message": "Movie has been created successfully"
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)
