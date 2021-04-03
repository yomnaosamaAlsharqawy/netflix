import json

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes

from resources.models import Tvshows, Casts, Moods, Genres
from resources.yomna_resources.serializers import TvshowsSerializer


class TvShowsController(APIView, ):
    def get(self, request, *args, **kwargs):
        try:
            tv_shows = Tvshows.objects.all()
            serializer = TvshowsSerializer(instance=tv_shows, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            moods = json.loads(data['moods'])
            genres = json.loads(data['genres'])
            tv_show = Tvshows(name=data['name'], description=data['description'], year=data['year'], age=data['age'],
                              image=data['image'], trailer=data['trailer'])
            tv_show.clean()
            tv_show.save()
            cast_data = json.loads(data['casts'])
            for i in cast_data:
                cast = Casts.objects.create(name=i['name'], role=i['role'])
                tv_show.casts.add(cast)
            for i in moods:
                mood = Moods.objects.get(mood=i)
                tv_show.moods.add(mood)
            for i in genres:
                genre = Genres.objects.get(genre=i)
                tv_show.genres.add(genre)

            return Response(data={
                "success": True,
                "message": "TV-show has been created successfully"
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)
