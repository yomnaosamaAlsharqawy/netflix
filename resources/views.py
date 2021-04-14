from rest_framework.permissions import IsAuthenticated

from .subviews.tvshows import *
from .subviews.Episodes import *
from .subviews.likes_dislikes import *
from .subviews.search import *
from .subviews.movies import MovieController

from .models import Movies, Tvshows, Casts, Country
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from .serializers import *


# end point to add new country
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


# select all country from model
@api_view(["GET", ])
def show_all_countries(request):
    country = Country.objects.all()
    serializer = CountrySerializer(instance=country, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# show all casts in database
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


# top ten of movies created in specific country
@api_view(["GET", ])
def top_ten_movies(request, country):
    movies = Movies.objects.order_by('views').reverse().filter(country__name=country)[:10]
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# top ten of tv-show created in specific country
@api_view(["GET", ])
def top_ten_tv_show(request, country):
    tv_show = Tvshows.objects.order_by('views').reverse().filter(country__name=country)[:10]
    serializer = TvshowsSerializer(instance=tv_show, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# filter in movies or tv-shows by [mood or genres or country or cast name]
class Filters(APIView):
    permission_classes = [IsAuthenticated, ]

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


# list all genres from model
@api_view(["GET"])
def show_all_genres(request):
    genres = Genres.objects.all()
    serializer = GenresSerializer(instance=genres, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class Suggestion(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        try:
            if request.GET['type'] == 'movie':
                movies = Movies.objects.filter(genres__genre=request.GET['genre']).exclude(id=request.GET['id'])
                serializer = MovieSerializer(instance=movies, many=True)
            else:
                tv_shows = Tvshows.objects.filter(genres__genre=request.GET['genre']).exclude(id=request.GET['id'])
                serializer = TvshowsSerializer(instance=tv_shows, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)
