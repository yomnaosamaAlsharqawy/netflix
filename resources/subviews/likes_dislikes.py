from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from resources.models import Tvshows, Movies


class Likes(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        data = request.data
        rate = int(data['rate'])
        try:
            if data['type'] == "movie":
                print(type(data['rate']))
                movie = Movies.objects.get(pk=data['id'])
                if rate == -1 and movie.likes != 0:
                    movie.likes = movie.likes - 1
                    movie.save()
                if rate == 1:
                    movie.likes = movie.likes + 1
                    movie.save()
                    print(movie.likes)
            else:
                tv_show = Tvshows.objects.get(pk=data['id'])
                if rate == -1 and tv_show.likes != 0:
                    tv_show.likes = tv_show.likes - 1
                    tv_show.save()
                if rate == 1:
                    tv_show.likes = tv_show.likes + 1
                    tv_show.save()

            return Response({'detail': 'updated'})
        except Exception as e:
            return Response({"detail": str(e)}, status=404)


class Views(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            if data['type'] == "movie":
                movie = Movies.objects.get(pk=data['id'])
                movie.views = movie.views + 1
                movie.save()
            else:
                tv_show = Tvshows.objects.get(pk=data['id'])
                tv_show.views = tv_show.views + 1
                tv_show.save()

            return Response({'detail': 'updated'})

        except Exception as e:
            return Response({"detail": str(e)}, status=404)
