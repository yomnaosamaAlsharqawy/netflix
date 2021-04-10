from rest_framework import serializers

from resources.serializers import MovieSerializer, TvshowsSerializer
from .models import *


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"

    movie = MovieSerializer(read_only=True)
    tv_show = TvshowsSerializer(read_only=True)
