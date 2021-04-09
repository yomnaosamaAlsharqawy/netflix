from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from mylist.models import List
from mylist.serializers import *


class ListController(APIView, ):
    def get(self, request, *args, **kwargs):
        try:
            list = List.objects.filter(profile__id=request.GET['id'])
            serializer = HistorySerializer(instance=list, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"detail": str(e)}, status=404)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            list = List(profile_id=data['profile'], movie_id=data.get('movie', None),
                        tv_show_id=data.get('tv_show', None))
            list.clean()
            list.save()
            return Response({"detail": "has been added successfully!"})
        except Exception as e:
            return Response({"detail": str(e)}, status=404)

    def delete(self, request, *args, **kwargs):
        try:
            data = request.data
            if data.get('movie'):
                list = List.objects.filter(profile_id=data['profile'], movie_id=data['movie'])
            else:
                list = List.objects.filter(profile_id=data['profile'], tv_show_id=data['tv_show'])
            list.delete()
            return Response({"detail": "has been deleted successfully!"})
        except Exception as e:
            return Response({"detail": str(e)}, status=404)
