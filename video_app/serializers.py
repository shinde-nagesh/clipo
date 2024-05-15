from rest_framework import serializers
from .models import VideoProject

class VideoProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoProject
        fields = '__all__'



# users/serializers.py

from rest_framework import serializers
from .models import CustomUser
# from .models import AllData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'phone_number' ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
