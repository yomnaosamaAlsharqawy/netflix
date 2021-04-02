from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import serializers


class PlanSerializer(serializers.ModelSerializer):
    pass


class PlanList(ListAPIView):
    pass
