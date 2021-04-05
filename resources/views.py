import io
import json

from django.shortcuts import render
from django.http import response, JsonResponse
from rest_framework.viewsets import ModelViewSet

from resources.models import Movies,Tvshows,Moods,Casts,Genres,Country
from resources.serializers import MovieSerializer,CastSerializer,CountrySerializer,TvshowsSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import  Response
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
# from resources.models import Snippet
# from resources.serializers import SnippetSerializer

#
# @api_view(['GET','POST'])
# def show_list(request):
#           if request.method == 'GET':
#                snippets = Snippet.objects.all()
#                serializer = SnippetSerializer(snippets, many=True)
#                return Response({
#                     'success': True,
#                     'data': serializer.data,
#                     'status':"ok"
#                })
#
#           elif request.method == 'POST':
#                data = JSONParser().parse(request)
#                serializer = SnippetSerializer(data=data)
#                if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data, status=status.HTTP_201_CREATED)
#                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class show_list(APIView):
#      def get(self, request, format=None):
#           snippets = Snippet.objects.all()
#           serializer = SnippetSerializer(snippets, many=True)
#           return Response({
#                          'success': True,
#                          'data': serializer.data,
#                          'status':"ok"
#                     })
#      def post(self, request, format=None):
#                data = JSONParser().parse(request)
#                serializer = SnippetSerializer(data=data)
#                if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data, status=status.HTTP_201_CREATED)
#                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#
# class show_list(mixins.ListModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
# class show_list(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#

def index(request):
     return response.HttpResponse("<h1>hello</h1>")

@api_view(["GET",])
def show_all_movies(request):
    movies = Movies.objects.all()
    serializer = MovieSerializer(instance=movies,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(["GET",])
def show_all_tv_shows(request):
    tv_shows = Tvshows.objects.all()
    serializer = TvshowsSerializer(instance=tv_shows,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(["POST",])
def create_movie(request):
        data_cast = request.data['casts']
        data_genre =  request.data['genres']
        data_mood =request.data['moods']
        country = Country.objects.get(name=request.data['country']['name'])
        movie = Movies.objects.create(
        name= request.data['name'], description= request.data['description'], time=request.data['time'],
            image=request.data['image'], year=request.data['year'], likes=request.data['likes'] , dislikes=request.data['dislikes']  , age=request.data['age']
            ,views= request.data['views'],trailer=request.data['trailer'],country=country)
        movie.clean()
        movie.save()

        instance = Movies.objects.get(pk=movie.id)

        for i in data_cast:
            cast = Casts.objects.create(name=i['name'],role=i["role"])
            instance.casts.add(cast)

        for k in data_genre:
            genre = Moods.objects.create(name=k['name'])
            instance.genres.add(genre)


        for j in data_mood:
            mood = Genres.objects.create(name=j["name"])
            movie.moods.add(mood)

        # instance.country = country
        # movie.casts.add(cast)
        # print(movie.casts)


        # serializer = MovieSerializer(data=request.data)
        # if serializer.is_valid():
        #     print(serializer.data)
        #     movie = Movies.objects.create(date=serializer.data)
        #     print(movie)
            # serializer.save()
        return Response(data={
                "success": True,
                "message": "Movie has been created successfully"
            }, status=status.HTTP_201_CREATED)
        #
        # return Response(data={
        #     "success": False,
        #     "errors": serializer.errors,
        # }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST",])
def create_tv_show(request):
    serializer = TvshowsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "Tv Show has been created successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors,
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST",])
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


@api_view(["GET",])
def show_all_countries(request):
    country = Country.objects.all()
    serializer = CountrySerializer(instance=country,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)



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


@api_view(["GET",])
def show_country_movies(request,country):
    movies = Movies.objects.filter(country__name=country)[:2]
    serializer = MovieSerializer(instance=movies,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(["GET",])
def show_country_tv_shows(request,country):
    tv_show = Tvshows.objects.filter(country__name=country)[:2]
    serializer = MovieSerializer(instance=tv_show,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(["GET",])
def top_ten_movies(request,country):
    movies = Movies.objects.order_by('views').reverse().filter(country__name=country)[:10]
    serializer = MovieSerializer(instance=movies,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(["GET",])
def top_ten_tv_show(request,country):
    tv_show = Tvshows.objects.order_by('views').reverse().filter(country__name=country)[:10]
    serializer = MovieSerializer(instance=tv_show,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


# class updatemovie(mixins.UpdateModelMixin,generics.GenericAPIView):
#         queryset = Movies.objects.all()
#         serializer_class = MovieSerializer
#
#         def put(self, request, *args, **kwargs):
#             return self.update(request, *args, **kwargs)


#
# class updatemovie(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movies.objects.all()
#     serializer_class = MovieSerializer


class updatemovie(APIView):
    def post(self, request, pk, format=None):
        data_cast = request.data['casts']
        data_genre = request.data['genres']
        data_mood = request.data['moods']
        country = Country.objects.get(name=request.data['country']['name'])
        movie = Movies.objects.get(pk=pk)
        movie.genres.clear()
        movie.moods.clear()
        movie.casts.clear()
        movie.country = country
        for i in data_cast:
            cast = Casts.objects.create(name=i['name'], role=i["role"])
            movie.casts.add(cast)

        for k in data_genre:
            genre = Moods.objects.filter(name=k['name']).first()
            movie.genres.add(genre)

        for j in data_mood:
            mood = Genres.objects.filter(name=j["name"]).first()
            movie.moods.add(mood)


        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            movie.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(["POST", ])
# def updatemovie(request,pk):
#         data_cast = request.data['casts']
#         data_genre = request.data['genres']
#         data_mood = request.data['moods']
#         country = Country.objects.get(name=request.data['country']['name'])
#         movie = Movies.objects.get(pk=pk)
#         movie.genres.clear()
#         movie.moods.clear()
#         movie.casts.clear()
#         movie.country = country
#         for i in data_cast:
#             cast = Casts.objects.create(name=i['name'], role=i["role"])
#             movie.casts.add(cast)
#
#         for k in data_genre:
#             genre = Moods.objects.filter(name=k['name']).first()
#             movie.genres.add(genre)
#
#         for j in data_mood:
#             mood = Genres.objects.filter(name=j["name"]).first()
#             movie.moods.add(mood)
#
#
#         serializer = MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             movie.save()
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(["POST", ])
def deletemovie(request,pk):
            movie = Movies.objects.get(pk=pk)
            movie.delete()
            return Response({"success":"deleted successfully"})