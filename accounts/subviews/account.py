from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework import status
from accounts.models import Account, Plan
from accounts.serializers import AccountRegisterSerializer, AccountRetrieveUpdateSerializer
from accounts.helpers import validate_email, validate_phone_number


@api_view(['POST', ])
def user_check(request):
    try:
        username = request.data.get('username', None)
        if username is None or not validate_email(username):
            return Response({
                'error': 'A valid email must be provided!'
            }, status=status.HTTP_400_BAD_REQUEST)
        account = Account.objects.get(username=username)
    except ObjectDoesNotExist:
        return Response({'exists': False}, status=status.HTTP_404_NOT_FOUND)
    return Response({
        'exists': True,
        'id': account.id,
    }, status=status.HTTP_200_OK)


class AccountRegister(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountRegisterSerializer


@api_view(['PATCH', ])
def add_plan(request):
    id = request.data.get('id', None)
    plan_id = request.data.get('plan_id', None)

    if id is None or id == '':
        return Response({
            'id': 'User id must be provided!'
        }, status=status.HTTP_400_BAD_REQUEST)

    if plan_id is None or plan_id == '':
        return Response({
            'plan_id': 'Plan id must be provided!'
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = Account.objects.get(pk=id)
    except ValueError:
        return Response({
            'id': 'User id is not valid'
        }, status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        return Response({
            'error': 'User not found!'
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        plan = Plan.objects.get(pk=plan_id)
    except ValueError:
        return Response({
            'plan_id': 'Plan id is not valid!'
        }, status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        return Response({
            'plan': 'Plan does not exist!'
        }, status=status.HTTP_404_NOT_FOUND)

    user.plan_id = plan
    user.registration_state = 3  # -> 'step3'
    user.save()

    return Response({
        'id': user.id,
        'username': user.username,
        'plan_id': plan.id,
        'registration_state': user.registration_state
    }, status=status.HTTP_200_OK)


@api_view(['PATCH', ])
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
            'phone_number': 'Phone number must be provided'
        }, status=status.HTTP_400_BAD_REQUEST)

    if country_code is None or country_code == '':
        return Response({
            'country_code': 'country code must be provided'
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = Account.objects.get(pk=id)
    except ValueError:
        return Response({
            'id': 'User id is not valid'
        }, status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        return Response({
            'error': 'User not found'
        }, status=status.HTTP_404_NOT_FOUND)

    if validate_phone_number(phone_number, country_code) is False:
        return Response ({
            'phone_number': 'Phone number is not valid!'
        }, status=status.HTTP_400_BAD_REQUEST
        )

    user.phone_number = phone_number
    user.registration_state = 4  # -> 'completed'
    user.save()

    return Response({
        'id': user.id,
        'username': user.username,
        'plan_id': user.plan_id.id,
        'phone_number': user.phone_number,
        'registration_state': user.registration_state
    }, status=status.HTTP_200_OK)


class AccountRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountRetrieveUpdateSerializer


