from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework import serializers
from rest_framework import status
from accounts.models import Account
from accounts.helpers import validate_phone_number
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


class AccountCreateStepOneSerializer(DynamicFieldsModelSerializer):
    password = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ('id', 'username', 'password', 'password1', 'registration_state')
        read_only_fields = ('registration_state', )

    def create(self, validated_data):
        username = validated_data.get('username', None)
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

        if username is None or not re.search(REGEX, username):
            raise serializers.ValidationError({
                'email': 'A valid email must be provided'
            })

        user = Account(
            username=username,
            password=password,
            registration_state=1
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


@api_view(['POST', ])
def add_phone_number(request):

    id = request.data.get('id', None)
    phone_number = request.data.get('phone_number', None)
    country_code = request.data.get('country_code', None)

    if id is None or id == '':
        return Response({
            'id': 'User id must be provided'
        }, status=status.HTTP_400_BAD_REQUEST)

    if phone_number is None or phone_number == '':
        return Response({
            'phone number': 'Phone number must be provided'
        }, status=status.HTTP_400_BAD_REQUEST)

    if country_code is None or country_code == '':
        return Response({
            'country_code': 'country code must be provided'
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = Account.objects.get(pk=id)
    except ObjectDoesNotExist:
        return Response({
            'error': 'User not found'
        }, status=status.HTTP_404_NOT_FOUND)

    if validate_phone_number(phone_number, country_code) is False:
        raise serializers.ValidationError(
            {'phone_number': 'Phone number is not valid!'}
        )

    user.phone_number = phone_number
    user.registration_stage = 4
    user.save()

    return Response({'message': 'Phone number Added Successfully'})


class AccountRegisterSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'phone_number', 'plan_id', 'groups')
        read_only_fields = ('plan_id', 'user_permissions', 'groups')


class AccountRegister(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountRegisterSerializer


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