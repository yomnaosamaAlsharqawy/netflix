from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import serializers
from accounts.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class PlanList(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
