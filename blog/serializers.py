from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.serializers import ModelSerializer
from django.utils.text import slugify

from blog.models import Post


class PostSerializer(ModelSerializer):
    """A serialize for our post list objects"""
    class Meta:
        model = Post
        fields = ('id', 'title')
        # fields = '__all__'


class DateRangeSerializer(Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()


class AddPostSerializer(ModelSerializer):
    """Creating Post"""
    class Meta:
        model = Post
        exclude = ('date', 'url')  # because auto now add = True

    def create(self, validated_data):  # validated_data = All fields are available here except date & url
        """Method overriding"""
        title = validated_data['title']
        slug_url = slugify(title)
        validated_data['url'] = slug_url
        return Post.objects.create(**validated_data)  # create is built-in
