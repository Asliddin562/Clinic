from rest_framework import serializers
from .models import Patient, MedicalHistory, PatientAddress


class PatientAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientAddress
        fields = ['region',
                  'district',
                  'street',
                  'home']


class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = [
            'id',
            'diagnosis',
            'description',
            'date',
            'image'
        ]



class GetPatientSerializer(serializers.ModelSerializer):
    address = PatientAddressSerializer()
    history = MedicalHistorySerializer()

    class Meta:
        model = Patient
        fields = [
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
            'address',
            'history'
        ]

    def create(self, validated_data):
        address_data = validated_data.pop('address', None)
        history_data = validated_data.pop('history', None)

        # agar address_data bo‘sh dict bo‘lsa, None qilamiz
        if not address_data or not any(address_data.values()):
            address_data = None

        if not history_data or not any(history_data.values()):
            history_data = None

        history = None
        if history_data:
            history = MedicalHistory.objects.create(**history_data)

        patient = Patient.objects.create(history=history, **validated_data)

        if address_data:
            address = PatientAddress.objects.create(**address_data)
            patient.address = address
            patient.save()

        return patient




