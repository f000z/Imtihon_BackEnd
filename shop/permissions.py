# permissions.py
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение, которое позволяет только владельцу объекта изменять или удалять его.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешение на чтение доступно всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешение на изменение или удаление доступно только владельцу
        return obj.user == request.user  # Проверка, что запрос был от владельца
