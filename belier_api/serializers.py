from django.contrib.auth.models import User, Group
from .models import ImageBelier
from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageBelier
        fields = ('title',
                  'image',
                  'get_category_display',)

