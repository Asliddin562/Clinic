from rest_framework import viewsets
from user.permissions import IsAdmin, IsDirector, IsDoctor
from  rest_framework.permissions import AllowAny
from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('-created_at')
    serializer_class = AppointmentSerializer
    permission_classes = [IsAdmin|IsDirector|IsDoctor|AllowAny]


