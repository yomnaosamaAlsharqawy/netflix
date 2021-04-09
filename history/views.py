from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from history.models import History
from history.serializer import HistorySerializer


class HistoryController(APIView, ):
    def get(self, request, *args, **kwargs):
        try:
            histories = History.objects.filter(profile__id=request.GET['id'])
            serializer = HistorySerializer(instance=histories, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            history = History(profile_id=data['profile'], movie_id=data.get('movie', None),
                              tv_show_id=data.get('tv_show', None))
            history.clean()
            history.save()
            return Response({"detail": "has been added successfully!"})
        except Exception as e:
            return Response({"detail": str(e)}, status=404)
