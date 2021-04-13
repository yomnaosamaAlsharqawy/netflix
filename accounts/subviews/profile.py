from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework import status
from accounts.models import Profile, ProfileImage, Account


class ProfileSerializer(serializers.ModelSerializer):
    # pin_code = serializers.CharField(write_only=True, allow_blank=True)

    class Meta:
        model = Profile
        fields = ['id', 'account_id', 'name', 'image_id', 'image_url', 'pin_code']
        read_only_fields = ['image_url', ]


class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = ['id', 'name', 'image_url']


class ProfileImageList(ListAPIView):
    queryset = ProfileImage.objects.all()
    serializer_class = ProfileImageSerializer
    lookup_field = 'pk'


@api_view(['POST', ])
def profile_login(request, profile_id):
    pin_code = request.data.get('pin_code', None)
    profile = Profile.objects.get(pk=profile_id)

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
    lookup_url_kwarg = 'account_id'

    def get_queryset(self):
        pk = self.kwargs.get(self.lookup_url_kwarg)
        print("***", pk)
        profiles = Account.objects.get(pk=pk).profiles
        print("***", profiles)
        return profiles


class ProfileCreate(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
