from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from resources.models import Seasons, Episodes
from resources.serializers import EpisodesSerializer


class EpisodeController(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        try:
            season = Seasons.objects.get(season=request.GET['season'], tv_show_id=request.GET['tv_show'])
            episodes = Episodes.objects.filter(season=season)
            serializer = EpisodesSerializer(instance=episodes, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            season = Seasons.objects.get(season=data['season'], tv_show_id=data['tv_show'])
            episode = Episodes(name=data['name'], description=data['description'], image=data['image'], url=data['url'],
                               time=data['time'],
                               season=season)
            episode.clean()
            episode.save()
            return Response(data={
                "success": True,
                "message": "TV-show's Episode has been created successfully"
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"detail": str(e)}, status=404)


class OneEpisode(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        try:
            episode = Episodes.objects.get(pk=request.GET['episode'])
            serializer = EpisodesSerializer(instance=episode)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)
