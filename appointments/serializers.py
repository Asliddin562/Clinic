from rest_framework import serializers
from patients.models import Patient, PatientAddress
from .models import Appointment
from patients.serializers import CreatePatientSerializer, PatientAddressSerializer
from employees.models import Employee

class AppointmentSerializer(serializers.ModelSerializer):
    patient = CreatePatientSerializer(required=False)
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), write_only=True, required=False
    )
    doctor = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.filter(is_accepting_appointments=True)
    )

    class Meta:
        model = Appointment
        fields = [
            'id',
            'doctor',
            'patient',
            'patient_id',
            'date',
            'start_time',
            'end_time',
            'status',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, attrs):
        if not attrs.get('patient') and not attrs.get('patient_id'):
            raise serializers.ValidationError("patient yoki patient_id kerak.")
        return attrs

    def create(self, validated_data):
        patient_data = validated_data.pop('patient', None)
        patient_id = validated_data.pop('patient_id', None)

        if patient_id:
            patient = patient_id
        elif patient_data:
            address_data = patient_data.pop('address')
            address = PatientAddress.objects.create(**address_data)
            patient = Patient.objects.create(address=address, **patient_data)
        else:
            raise serializers.ValidationError("patient yoki patient_id kerak.")

        appointment = Appointment.objects.create(patient=patient, **validated_data)
        return appointment
