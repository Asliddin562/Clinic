from rest_framework import serializers
from .models import Patient, MedicalHistory, PatientAddress


class PatientAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientAddress
        fields = ['id',
                  'patient',
                  'region',
                  'district',
                  'street',
                  'home']


class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = [
            'id',
            'patient',
            'diagnosis',
            'description',
            'date',
            'image'
        ]



class GetPatientSerializer(serializers.ModelSerializer):
    address = PatientAddressSerializer(read_only=True)
    history = MedicalHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = [
            'id',
            'card_number',
            'first_name',
            'last_name',
            'father_name',
            'birth_date',
            'gender',
            'phone',
            'address',
            'history',
        ]


class CreatePatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = [
            'id',
            'first_name',
            'last_name',
            'father_name',
            'birth_date',
            'gender',
            'phone',
        ]




