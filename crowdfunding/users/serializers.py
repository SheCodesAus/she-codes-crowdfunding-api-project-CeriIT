from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(
        validators=[
        UniqueValidator(
            queryset=CustomUser.objects.all(),
            message=("Name already exists")
            )
        ]
    )
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)

    
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)