from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from mylist.models import List
from mylist.serializers import *


class ListController(APIView, ):
    permission_classes = [IsAuthenticated, ]

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
            # mylist = List.objects.filter(profile_id=data['profile']).filter(
            #     Q(movie_id=data.get('movie', None)) | Q(tv_show_id=data.get('tv_show', None)))
            # if mylist:
            #     return Response({"detail": "has been added successfully!"})
            # else:
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
