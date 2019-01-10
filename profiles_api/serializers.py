from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.serializers import ModelSerializer

# Same App importing
from profiles_api.models import UserProfile


# class HelloSerializer(ModelSerializer):
class HelloSerializer(Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)

    # class Meta:
    #     model = UserProfile
    #     fields = '__all__'

