from rest_framework import viewsets
from .models import Patient, MedicalHistory
from user.permissions import IsDirector, IsAdmin, IsDoctor
from rest_framework.permissions import AllowAny
from rest_framework import filters
from .serializers import (
    GetPatientSerializer,
    CreatePatientSerializer,
    MedicalHistorySerializer
)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    permission_classes = [IsDirector | IsAdmin | IsDoctor | AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['patient__first_name', 'patient__last_name']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return GetPatientSerializer
        return CreatePatientSerializer



class MedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer
    permission_classes = [IsDirector|IsAdmin|IsDoctor|AllowAny]

