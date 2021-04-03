from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework import serializers
from rest_framework import status
from accounts.models import Account
from django.core.validators import validate_email
import re

REGEX = '^(\w|.|_|-)+[@](\w|_|-|.)+[.]\w{2,3}$'


#https://stackoverflow.com/questions/44063644/django-rest-framework-serializer-different-fields-in-multiple-views
class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` and 'exclude' argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if exclude is not None:
            not_allowed = set(exclude)
            for exclude_name in not_allowed:
                self.fields.pop(exclude_name)


class AccountCreateSerializer(DynamicFieldsModelSerializer):
    password = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ('email', 'password', 'password1')

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


class AccountUpdateSerializer(DynamicFieldsModelSerializer):
    password = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        exclude = ('registration_state', 'last_login')


class AccountCreate(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer


class AccountRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountUpdateSerializer


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