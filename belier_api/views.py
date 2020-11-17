from django.contrib.auth.models import User, Group

import base64
from PIL import Image
from io import BytesIO
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.models import Token

from rest_framework.parsers import MultiPartParser, FormParser

from django.db.models.query import QuerySet

from .models import ImageBelier
from rest_framework.views import APIView 
from belier_api.serializers import PhotoSerializer


class PhotoList(APIView):

    permission_classes = (permissions.AllowAny,)
    parser_classes = (MultiPartParser, FormParser)
    http_method_names = ['get', 'head', 'post', 'delete']


    def get(self, request, *args, **kwargs):
        image = ImageBelier.objects.all()
        
        serializer = PhotoSerializer(image, many=True, context={"request":request})
        if request.method == "GET":
            for img in image:
                if img.image is None:
                    fh = img.image.path
                    # fh = img.image.storage.location + '/' + img.title
                    img.image = Image.open(BytesIO(base64.b64decode(img.image_64)))
                    img.save()
                
                # serializer.data('image') += img.image
                # img.save(fh, 'JPEG')
                # imgdata = base64.b64decode(img.image_64)
                # with open(fh, 'wb') as f:
                #     f.write(imgdata)
                #     f.close()
        
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        image_serializer = PhotoSerializer(data=request.data)
        if request.method == "POST":
            if request.POST.get('token'):
                token = Token.objects.get(key=request.POST.get('token'))
                if token:
                    if image_serializer.is_valid():
                        image_serializer.save()
                        img = image_serializer['image']
                        modelImageBelier = ImageBelier.objects.last()
                        
                        with open(modelImageBelier.image.path, 'rb') as fileImage:
                            modelImageBelier.image_64 = base64.b64encode(fileImage.read())
                            modelImageBelier.image_64 = modelImageBelier.image_64.decode('utf-8')    
                        modelImageBelier.save()
                        return Response(image_serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        print('error', image_serializer.errors)
                        return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return HttpResponse('Unauthorized', status=401)

