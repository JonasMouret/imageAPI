from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from .models import ImageBelier
from rest_framework.views import APIView 
from belier_api.serializers import PhotoSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]

class PhotoList(APIView):

    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head']

    # queryset = ImageBelier.objects.all()
    # serializer_class = PhotoSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        serializer = PhotoSerializer(ImageBelier.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def get(self, request):
    #     '''
    #     Get Image
    #     '''
    #     try:
    #         picture = ImageBelier.objects.all()
    #     except Picture.DoesNotExist:
    #         raise Http404

    #     serialiser = PhotoSerializer(picture)
    #     return Response(serialiser.data)
