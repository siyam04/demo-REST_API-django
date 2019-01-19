from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.serializers import ModelSerializer

# Same App importing
from profiles_api.models import UserProfile, ProfileFeedItem


class HelloSerializer(Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(ModelSerializer):
    """A serialize for our user profile objects"""
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        # Password field is write-only
        extra_kwargs = {'password': {'write_only': True}}
        # fields = '__all__'

    def create(self, validated_data):
        """Create and return a new user"""
        try:
            user = UserProfile(name=validated_data['name'], email=validated_data['email'])
            user.set_password(validated_data['password'])
            user.save()
            return user

        except NotImplementedError:
            print('create() must be implemented.')


class ProfileFeedItemSerializer(ModelSerializer):
    """A serializer for profile feed items"""
    class Meta:
        model = ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        # user_profile field is read-only
        extra_kwargs = {'user_profile': {'read_only': True}}
        # fields = '__all__'


