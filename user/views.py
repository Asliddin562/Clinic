from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from user.permissions import IsDirector
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (CreateUserRegisterSerializer,
                          UserRegisterSerializer,
                          UserRoleUpdateSerializer,
                          CustomTokenObtainPairSerializer)

User = get_user_model()

class UserRegisterViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    permission_classes = [AllowAny | IsDirector]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return UserRegisterSerializer
        return CreateUserRegisterSerializer


class UserRoleUpdateViewSet(
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserRoleUpdateSerializer
    permission_classes = [IsDirector|AllowAny]



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [IsDirector | AllowAny]

