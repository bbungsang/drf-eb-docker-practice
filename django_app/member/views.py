from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

from member.models import MyUser
from member.permissions import OwnerOrReadOnly
from member.serializers import UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        # 로그인을 안 하면, 읽기만 할 수 있다.
        permissions.IsAuthenticatedOrReadOnly,
        OwnerOrReadOnly,
    )
