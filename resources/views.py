from rest_framework.response import Response
from rest_framework.views import APIView
from .subviews.tvshows import TvShowsController
from .subviews.movies import MovieController

from .models import Movies, Tvshows, Episodes, Casts, Country
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from .serializers import MovieSerializer, CountrySerializer, CastSerializer
from .yomna_resources.serializers import TvshowsSerializer, EpisodesSerializer, TvshowsdetailedSerializer


class ListByGenres(APIView, ):
    def get(self, request, genre, type, *args, **kwargs):
        try:
            if type == "movie":
                movies = Movies.objects.filter(genres__genre=genre)
                serializer = MovieSerializer(instance=movies, many=True)
            else:
                tvshows = Tvshows.objects.filter(genres__genre=genre)
                serializer = TvshowsSerializer(instance=tvshows, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)


class ListEpisodes(APIView, ):
    def get(self, request, index, *args, **kwargs):
        try:
            episodes = Episodes.objects.filter(season__season=index)
            serializer = EpisodesSerializer(instance=episodes, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)



class ListByMoods(APIView, ):
    def get(self, request, mood, type, *args, **kwargs):
        try:
            if type == "movie":
                movies = Movies.objects.filter(moods__mood=mood)
                serializer = MovieSerializer(instance=movies, many=True)
            else:
                tvshows = Tvshows.objects.filter(moods__mood=mood)
                serializer = TvshowsSerializer(instance=tvshows, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)


class ListByCasts(APIView, ):
    def get(self, request, cast, type, *args, **kwargs):
        try:
            if type == "movie":
                movies = Movies.objects.filter(casts__name=cast)
                serializer = MovieSerializer(instance=movies, many=True)
            else:
                tvshows = Tvshows.objects.filter(casts__name=cast)
                serializer = TvshowsSerializer(instance=tvshows, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)


class RecentlyAdded(APIView, ):
    def get(self,request,type,*args,**kwargs):
        try:
            if type == "movie":
                movies = Movies.objects.order_by('year').reverse()[:20]
                serializer = MovieSerializer(instance=movies, many=True)
            else:
                tvshows = Tvshows.objects.order_by('year').reverse()[:20]
                serializer = TvshowsSerializer(instance=tvshows, many=True)
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
def show_country_movies(request, country):
    print(country)
    movies = Movies.objects.filter(country__name=country)
    print(movies)
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    # print(request)
    # return Response({"detail": "koko"})


@api_view(["GET", ])
def show_country_tv_shows(request, country):
    tv_show = Tvshows.objects.filter(country__name=country)[:2]
    serializer = TvshowsSerializer(instance=tv_show, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


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
