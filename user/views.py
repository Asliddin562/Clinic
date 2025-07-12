from rest_framework import mixins, viewsets, status
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.utils.translation import gettext_lazy as _
from user.permissions import IsDirector
from .serializers import CreateUserRegisterSerializer, UserRegisterSerializer, UserRoleUpdateSerializer, AccessTokenSerializer

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


class UserFromAccessTokenAPIView(GenericAPIView):
    serializer_class = AccessTokenSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        access_token = serializer.validated_data["access"]

        try:
            token = AccessToken(access_token)
            user_id = token["user_id"]
            user = User.objects.get(id=user_id)
        except Exception:
            return Response({"detail": _("Invalid token.")}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "first_name": user.first_name,
            "last_name": user.last_name
        }, status=status.HTTP_200_OK)
