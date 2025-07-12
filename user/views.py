from rest_framework import mixins, viewsets, status
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model, authenticate
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.utils.translation import gettext_lazy as _
from user.permissions import IsDirector
from .serializers import CreateUserRegisterSerializer, UserRegisterSerializer, UserRoleUpdateSerializer, LoginOnlySerializer

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


class CheckLoginAPIView(GenericAPIView):
    serializer_class = LoginOnlySerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        if user:
            user_data = UserRegisterSerializer(user).data
            return Response(user_data, status=status.HTTP_200_OK)

        return Response(
            {"detail": _("This user is not registered yet!")},
            status=status.HTTP_404_NOT_FOUND
        )