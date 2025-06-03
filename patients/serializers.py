import re
from rest_framework import serializers
from django.utils.translation import  gettext_lazy as _
from .models import Patient, MedicalHistory, PatientAddress


class PatientAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientAddress
        fields = [
            'id',
            'patient',
            'region',
            'district',
            'street',
            'building',
            'apartment',
        ]


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
            'mobile_phone1',
            'mobile_phone2',
            'home_phone',
            'balance_amount',
            'comment',
            'extra_comment',
            'patient_recommendation',
            'future_appointment',
            'treated_doctors',
            'address',
            'history'
        ]
        read_only_fields = ['created_at', 'updated_at']


PHONE_REGEX = r'^\+998\d{9}$'

def normalize_phone(value):
    """Raqamni normal formatga keltiradi: +998XXXXXXXXX"""
    if value.startswith('998') and len(value) == 12:
        value = '+' + value
    return value


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
            'mobile_phone1',
            'mobile_phone2',
            'home_phone',
            'balance_amount',
            'comment',
            'extra_comment',
            'patient_recommendation',
            'future_appointment',
            'treated_doctors',
        ]

    def validate_mobile_phone1(self, value):
        value = normalize_phone(value)
        if not re.match(PHONE_REGEX, value):
            raise serializers.ValidationError(
                _("Asosiy mobil raqam '+998901234567' yoki '998901234567' formatida bo‘lishi kerak."))
        return value

    def validate_mobile_phone2(self, value):
        if value:
            value = normalize_phone(value)
            if not re.match(PHONE_REGEX, value):
                raise serializers.ValidationError(
                    _("Ikkinchi mobil raqam '+998901234567' yoki '998901234567' formatida bo‘lishi kerak."))
        return value

    def validate_home_phone(self, value):
        if value:
            value = normalize_phone(value)
            if not re.match(PHONE_REGEX, value):
                raise serializers.ValidationError(
                    _("Uy telefoni '+998901234567' yoki '998901234567' formatida bo‘lishi kerak."))
        return value


