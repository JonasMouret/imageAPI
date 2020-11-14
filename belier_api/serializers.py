from django.contrib.auth.models import User, Group
from .models import ImageBelier
from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']

# class PhotoSerializer(serializers.ModelSerializer):

#     image_url = serializers.SerializerMethodField('get_image_url')

#     class Meta:
#         model = ImageBelier
#         fields = ('title', 'image', 'image_url')

#     def get_image_url(self, obj, request):
#         request = self.context.get('request')
#         photo_url = obj.image.url
#         return request.build_absolute_uri(photo_url)


class PhotoSerializer(serializers.ModelSerializer):


    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = ImageBelier
        fields = ('title',
                  'image',
                  'image_url')

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)