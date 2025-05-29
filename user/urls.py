from django.urls import path
from .views import UserRegisterView, UserListAPIView, UserRetrieveUpdateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateAPIView.as_view(), name='user-update'),
    # path('', UserListAPIView.as_view(), name='user-list'),
    # path('change-role/<int:pk>/', ChangeUserRoleView.as_view(), name='change-user-role'),
]
