from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework import serializers


@api_view(["GET", ])
def test(request):
    return Response({"message": "It's working"})


class AccountSerializer(serializers.ModelSerializer):
    pass


class AccountCreate(CreateAPIView):
    pass


class AccountRetrieveUpdate(RetrieveUpdateAPIView):
    pass


class AccountCheck(RetrieveAPIView):
    pass
