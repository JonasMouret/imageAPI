from django.contrib.auth.models import User, Group
from .models import ImageBelier
import base64
from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageBelier
        fields = ('id', 'title', 'image', 'category', 'image_64')

