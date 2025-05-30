from rest_framework import viewsets
from .models import Patient, MedicalHistory, PatientAddress
from user.permissions import IsDirector, IsAdmin, IsDoctor
from rest_framework.permissions import AllowAny
from .serializers import (
    PatientAddressSerializer,
    GetPatientSerializer,
    CreatePatientSerializer,
    MedicalHistorySerializer
)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    permission_classes = [IsDirector | IsAdmin | IsDoctor | AllowAny]
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CreatePatientSerializer
        return GetPatientSerializer


class PatientAddressViewSet(viewsets.ModelViewSet):
    queryset = PatientAddress.objects.all()
    serializer_class = PatientAddressSerializer
    permission_classes = [IsDirector|IsAdmin|AllowAny]


class MedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer
    permission_classes = [IsDirector|IsAdmin|IsDoctor|AllowAny]



