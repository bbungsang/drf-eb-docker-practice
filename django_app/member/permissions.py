from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS 에 대한 요청 모두 True
        if request.method in permissions.SAFE_METHODS:
            return True
        # 로그인 한 유저만 접근 가능
        return obj == request.user
