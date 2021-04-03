from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework import status
from accounts.models.profile import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['account_id', 'id', 'name', 'image']


@api_view(['POST', ])
def profile_login(request, pk):
    pin_code = request.data.get('pin_code', None)
    profile = Profile.objects.get(pk=pk)

    if pin_code != profile.pin_code:
        return Response(data={
            "success": False,
            "message": "Incorrect Pin Code"
        }, status=status.HTTP_401_UNAUTHORIZED)

    return Response(data={
        "success": True,
        "message": "Profile Login Successful"
    }, status=status.HTTP_200_OK)


class ProfileList(ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self, request, id):
        return Profile.objects.filter(pk=id)


class ProfileCreate(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileRUD(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

