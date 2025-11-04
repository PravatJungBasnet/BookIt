from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "phone_number", "address", "role"]
        read_only_fields = ["id"]


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "email", "password", "phone_number", "address"]
