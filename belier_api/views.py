from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from rest_framework.parsers import MultiPartParser, FormParser

from django.db.models.query import QuerySet

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

# class PhotoList(APIView):

#     permission_classes = (permissions.AllowAny,)
#     http_method_names = ['get', 'head', 'post']

#     # queryset = ImageBelier.objects.all()
#     # serializer_class = PhotoSerializer
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get(self, request, *args, **kwargs):
#         serializer = PhotoSerializer(ImageBelier.objects.all(), many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post (self, request, format=None):
#         self.http_method_names.append("GET")
#         serializer = PhotoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PhotoList(APIView):

#     parser_classes = (MultiPartParser, FormParser)

#     # queryset = ImageBelier.objects.all()
#     # serializer_class = PhotoSerializer
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get(self, request, *args, **kwargs):
#         image = ImageBelier.objects.all()
#         serializer = PhotoSerializer(image, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         image_serializer = PhotoSerializer(data=request.data)
#         if image_serializer.is_valid():
#             image_serializer.save()
#             return Response(image_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print('error', image_serializer.errors)
#             return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhotoList(APIView):
    
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']


    def get(self, request, *args, **kwargs):
        image = ImageBelier.objects.all()
        serializer = PhotoSerializer(image, many=True, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        image_serializer = PhotoSerializer(data=request.data)
        if image_serializer.is_valid():
            image_serializer.save()
            return Response(image_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', image_serializer.errors)
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
