from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework import serializers
from rest_framework import status
from accounts.models.account import Account
from django.core.validators import validate_email
import re

REGEX = '^(\w|.|_|-)+[@](\w|_|-|.)+[.]\w{2,3}$'

@api_view(['POST', ])
def email_check(request):
    try:
        email = request.data.get('email', None)
        if email is None or not re.search(REGEX, email):
            return Response({'error': 'A valid email must be provided!'}, status=status.HTTP_400_BAD_REQUEST)
        Account.objects.get(email=email)
    except ObjectDoesNotExist:
        return Response({'exists': False}, status=status.HTTP_404_NOT_FOUND)

    return Response({'exists': True}, status=status.HTTP_200_OK)


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'password', 'password1']

    def create(self, validated_data):
        email = validated_data.get('email', None)
        password = validated_data.get('password', None)
        password1 = validated_data.get('password', None)

        if password is None:
            raise serializers.ValidationError({
                'password': 'Password must be provided'
            })

        if password1 is None or password != password1:
            raise serializers.ValidationError({
                'password1': "Passwords don't match"
            })

        if email is None:
            raise serializers.ValidationError({
                'email': 'A valid email must be provided'
            })

        return Account.objects.create(email=email, password=password)


class AccountCreate(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
