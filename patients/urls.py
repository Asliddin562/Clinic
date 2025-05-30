from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, MedicalHistoryViewSet, PatientAddressViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet, basename='patients')
router.register('patient-address', PatientAddressViewSet, basename='patient-address')
router.register('patient-histories', MedicalHistoryViewSet, basename='histories')

urlpatterns = [
    path('', include(router.urls)),
]
