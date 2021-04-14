import random

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from resources.models import Tvshows, Movies
from itertools import chain

from resources.serializers import MovieSerializer, TvshowsSerializer


class HomePageGenerator(APIView, ):
    permission_classes = [IsAuthenticated, ]
    def get(self, request, *args, **kwargs):
        # options_dict = {'mood': 'moods__mood', 'genre': 'genres__genre', 'country': 'country__name'}
        try:
            data = request.GET
            movies = Movies.objects.filter(genres__genre=data.get('genre')).distinct()
            tv_shows = Tvshows.objects.filter(genres__genre=data.get('genre')).distinct()
            serializer1 = TvshowsSerializer(instance=tv_shows, many=True)
            serializer2 = MovieSerializer(instance=movies, many=True)
            all = chain(serializer1.data, serializer2.data)
            all2 = list(all)
            random.shuffle(all2)
            return Response(all2, status=200)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)


class Popular(APIView, ):
    def get(self, request, *args, **kwargs):
        try:
            movies = Movies.objects.all().order_by('views')[:10]
            tv_shows = Tvshows.objects.all().order_by('views')[:10]
            serializer1 = TvshowsSerializer(instance=tv_shows, many=True)
            serializer2 = MovieSerializer(instance=movies, many=True)
            all = chain(serializer1.data, serializer2.data)
            all2 = list(all)
            random.shuffle(all2)
            return Response(all2, status=200)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)
