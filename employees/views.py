from rest_framework import viewsets, mixins
from .models import Employee, EmployeeAddress, WorkSchedule, Profession
from user.permissions import IsDirector
from django_filters.rest_framework import DjangoFilterBackend
from employees.filters import EmployeeFilter
from rest_framework.permissions import AllowAny
from .serializers import (
    EmployeeCreateSerializer,
    EmployeeGetSerializer,
    EmployeeAddressSerializer,
    WorkScheduleSerializer,
    ProfessionSerializer
)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter
    permission_classes = [IsDirector|AllowAny]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return EmployeeCreateSerializer
        return EmployeeGetSerializer

class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = [IsDirector|AllowAny]


class EmployeeAddressViewSet(viewsets.ModelViewSet):
    queryset = EmployeeAddress.objects.all()
    serializer_class = EmployeeAddressSerializer
    permission_classes = [IsDirector | AllowAny]


class WorkScheduleViewSet(viewsets.ModelViewSet):
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer
    permission_classes = [IsDirector | AllowAny]
