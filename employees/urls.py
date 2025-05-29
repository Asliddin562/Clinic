from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employees')
# router.register('work-schedule', WorkScheduleViewSet, basename='work-schedule')

urlpatterns = [
    path('', include(router.urls)),
]
