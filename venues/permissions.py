from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsownerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_staff or request.user.is_superuser:
            return True
        return obj.owner == request.user
