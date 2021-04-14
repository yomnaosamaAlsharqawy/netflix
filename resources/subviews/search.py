import random

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from resources.models import Tvshows, Movies
from django.db.models import Q
from itertools import chain

from resources.serializers import MovieSerializer, TvshowsSerializer, TvshowsdetailedSerializer, MovieInfoSerializer


class Search(APIView, ):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        try:
            data = request.GET
            name = data.get('name', '')
            genre = data.get('genre', None)
            movies = Movies.objects.filter(Q(name__icontains=name) | Q(genres__genre=genre)).distinct()
            tv_shows = Tvshows.objects.filter(Q(name__icontains=name) | Q(genres__genre=genre)).distinct()
            serializer1 = TvshowsSerializer(instance=tv_shows, many=True)
            serializer2 = MovieSerializer(instance=movies, many=True)
            all = chain(serializer1.data, serializer2.data)
            all2 = list(all)
            random.shuffle(all2)
            return Response(all2)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)


class MoreInfo(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        data = request.GET
        print(data.get('name'))
        try:
            if data.get('type') == 'tv_show':
                tv_show = Tvshows.objects.get(id=int(data.get('id')))
                serializer = TvshowsdetailedSerializer(instance=tv_show)
            else:
                movie = Movies.objects.get(id=data.get('id'))
                serializer = MovieInfoSerializer(instance=movie)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)
