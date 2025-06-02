from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, EmployeeAddressViewSet, WorkScheduleViewSet, ProfessionViewSet

router = DefaultRouter()
router.register('profession', ProfessionViewSet, basename='profession')
router.register('employees', EmployeeViewSet, basename='employee')
router.register('employee-address', EmployeeAddressViewSet, basename='employee-addresse')
router.register('employee-schedule', WorkScheduleViewSet, basename='employee-schedule')

urlpatterns = [
    path('', include(router.urls)),
]
