from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, MedicalHistoryViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet, basename='patient')
router.register('histories', MedicalHistoryViewSet, basename='history')

urlpatterns = [
    path('', include(router.urls)),
]
