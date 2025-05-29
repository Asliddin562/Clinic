from rest_framework import generics
from rest_framework.permissions import AllowAny
from user.permissions import IsDirector
from .serializers import UserRegisterSerializer, UserDetailSerializer
from rest_framework.views import APIView
from user.models import User

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [IsDirector|AllowAny]


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsDirector|AllowAny]


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsDirector|AllowAny]

