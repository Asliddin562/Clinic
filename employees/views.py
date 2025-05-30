from rest_framework import viewsets, mixins
from .models import Employee, EmployeeAddress, WorkSchedule
from .serializers import (
    EmployeeCreateSerializer,
    EmployeeGetSerializer,
    EmployeeAddressSerializer,
    WorkScheduleSerializer
)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return EmployeeCreateSerializer
        return EmployeeGetSerializer


class EmployeeAddressViewSet(viewsets.ModelViewSet):
    queryset = EmployeeAddress.objects.all()
    serializer_class = EmployeeAddressSerializer


class WorkScheduleViewSet(viewsets.ModelViewSet):
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer
