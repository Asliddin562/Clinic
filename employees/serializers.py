import re
from rest_framework import serializers
from .models import EmployeeAddress, WorkSchedule, Employee, Profession
from django.utils.translation import gettext_lazy as _
from user.models import User


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'name', 'code']

class WorkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSchedule
        fields = ['id',
                  'employee',
                  'monday',
                  'tuesday',
                  'wednesday',
                  'thursday',
                  'friday',
                  'saturday',
                  'sunday']


class EmployeeAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAddress
        fields = [
            'id',
            'employee',
            'region',
            'district',
            'street',
            'building',
            'apartment',
        ]


class EmployeeGetSerializer(serializers.ModelSerializer):
    address = EmployeeAddressSerializer(read_only=True)
    schedule = WorkScheduleSerializer(read_only=True)
    # profession = ProfessionSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = [
            'id',
            'user',
            'first_name',
            'last_name',
            'father_name',
            'mobile_phone1',
            'mobile_phone2',
            'home_phone',
            'birth_date',
            'email',
            'gender',
            'profession',
            'is_accepting_appointments',
            'earning_type',
            'commission_percentage',
            'fixed_salary',
            'is_working',
            'is_using_program',
            'passport_id',
            'chair',
            'color_hex',
            'comment',
            'address',
            'schedule',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']



PHONE_REGEX = r'^\+998\d{9}$'

def normalize_phone(value):
    """Raqamni normal formatga keltiradi: +998XXXXXXXXX"""
    if value.startswith('998') and len(value) == 12:
        value = '+' + value
    return value


class EmployeeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = [
            'id',
            'user',
            'first_name',
            'last_name',
            'father_name',
            'mobile_phone1',
            'mobile_phone2',
            'home_phone',
            'birth_date',
            'email',
            'gender',
            'profession',
            'is_accepting_appointments',
            'earning_type',
            'commission_percentage',
            'fixed_salary',
            'is_working',
            'is_using_program',
            'passport_id',
            'chair',
            'color_hex',
            'comment',
            'created_at',
            'updated_at',
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
