from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, UserRegisterSerializer
from .models import User

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        serializer_mapping = {
            "create": UserRegisterSerializer,
            "list": UserSerializer,
            "profile": UserSerializer,
        }
        return serializer_mapping.get(self.action)
    def create(self,request):
        data=request.data
        serializer=self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        user=serializer.save()
        user.set_password(data["password"])
        user.save()
        return Response(status=status.HTTP_200_OK)