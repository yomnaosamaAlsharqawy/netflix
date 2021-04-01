from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response

from resources.models import *
from resources.yomna_resources.serializers import TvshowsdetailedSerializer


@api_view(["GET", ])
def tvshowdetail(request, index):
    tv_show = Tvshows.objects.get(id=index)
    print(tv_show)
    serializer = TvshowsdetailedSerializer(tv_show)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
