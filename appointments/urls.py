from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, DoctorAppointmentsViewSet

router = DefaultRouter()
router.register('appointments', AppointmentViewSet, basename='appointments')
router.register('doctor-appointments', DoctorAppointmentsViewSet, basename='doctor-appointments')

urlpatterns = [
    path('', include(router.urls)),
]
