from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    pass


class ProfileList(ListAPIView):
    pass


class ProfileCreate(CreateAPIView):
    pass


class ProfileRUD(RetrieveUpdateDestroyAPIView):
    pass

