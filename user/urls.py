from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegisterViewSet, UserRoleUpdateViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('user-register', UserRegisterViewSet, basename='user-register')
router.register('user-change-role', UserRoleUpdateViewSet, basename='user-change-role')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
