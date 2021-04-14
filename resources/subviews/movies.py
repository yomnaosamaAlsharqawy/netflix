import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from resources.models import Casts, Moods, Genres, Movies, Country
from resources.serializers import MovieSerializer


class MovieController(APIView, ):
    permission_classes = [IsAuthenticated, ]
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
            country = Country.objects.get(name=request.data['country'])
            movie = Movies(name=data['name'], description=data['description'], year=data['year'], age=data['age'],
                           image=data['image'], trailer=data['trailer'], time=data['time'], url=data['url'], country=country)
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

    def put(self, request, *args, **kwargs):
        data_cast = json.loads(request.data['casts'])
        data_genre = json.loads(request.data['genres'])
        data_mood = json.loads(request.data['moods'])
        country = Country.objects.get(name=json.loads(request.data['country'])['name'])
        movie = Movies.objects.get(pk=request.data['id'])
        movie.genres.clear()
        movie.moods.clear()
        movie.casts.clear()
        movie.country = country
        for i in data_cast:
            cast = Casts.objects.create(name=i['name'], role=i["role"])
            movie.casts.add(cast)

        for k in data_genre:
            genre = Genres.objects.filter(genre=k['genre']).first()
            movie.genres.add(genre)

        for j in data_mood:
            mood = Moods.objects.filter(mood=j["mood"]).first()
            movie.moods.add(mood)

        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            movie.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        movie = Movies.objects.get(pk=request.GET['id'])
        movie.delete()
        return Response({"success": "deleted successfully"})
