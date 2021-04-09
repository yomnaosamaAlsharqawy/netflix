from rest_framework.response import Response
from rest_framework.views import APIView
from .subviews.tvshows import *
from .subviews.Episodes import *
from .subviews.likes_dislikes import *
from .subviews.search import *
from .subviews.movies import MovieController

from .models import Movies, Tvshows, Episodes, Casts, Country
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from .serializers import MovieSerializer, CountrySerializer, CastSerializer, EpisodesSerializer, TvshowsSerializer, \
    GenresSerializer


class ListEpisodes(APIView, ):
    def get(self, request, index, *args, **kwargs):
        try:
            episodes = Episodes.objects.filter(season__season=index)
            serializer = EpisodesSerializer(instance=episodes, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)


@api_view(["POST", ])
def add_country(request):
    serializer = CountrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "country has been added successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors,
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", ])
def show_all_countries(request):
    country = Country.objects.all()
    serializer = CountrySerializer(instance=country, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", ])
def show_all_casts(request):
    casts = Casts.objects.all()
    serializer = CastSerializer(instance=casts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST", ])
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


@api_view(["GET", ])
def top_ten_movies(request, country):
    movies = Movies.objects.order_by('views').reverse().filter(country__name=country)[:10]
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", ])
def top_ten_tv_show(request, country):
    tv_show = Tvshows.objects.order_by('views').reverse().filter(country__name=country)[:10]
    serializer = TvshowsSerializer(instance=tv_show, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class Filters(APIView):
    def get(self, request, *args, **kwargs):
        options_dict = {'mood': 'moods__mood', 'genre': 'genres__genre', 'cast': 'casts__name',
                        'country': 'country__name'}
        try:
            data = request.GET
            type = data['type']
            option = options_dict.get(data['option'], None)
            value = data['value']
            filters = {option: value}
            if type == 'movie':
                movies = Movies.objects.filter(**filters)
                serializer = MovieSerializer(instance=movies, many=True)
            else:
                tv_shows = Tvshows.objects.filter(**filters)
                serializer = TvshowsSerializer(instance=tv_shows, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)


@api_view(["GET"])
def show_all_genres(request):
    genres = Genres.objects.all()
    serializer = GenresSerializer(instance=genres, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
