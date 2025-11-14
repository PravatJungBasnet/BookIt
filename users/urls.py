from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, GoogleLogin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "users"
router = DefaultRouter()
router.register("", UserViewSet, basename="users")

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("google/", GoogleLogin.as_view(), name="google_login"),
]

urlpatterns += router.urls
