from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ToDo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ["id", "title", "is_done"]