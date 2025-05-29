from rest_framework import viewsets
from .models import Employee, WorkSchedule
from .serializers import EmployeeSerializer
from rest_framework.permissions import AllowAny
from user.permissions import IsDirector, IsAdmin

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdmin|IsDirector|AllowAny]



