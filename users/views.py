from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

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

    def create(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        user.set_password(data["password"])
        user.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET", "PUT", "PATCH"], name="View/Update Profile")
    def profile(self, request):
        user = request.user
        if request.method == "GET":
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
