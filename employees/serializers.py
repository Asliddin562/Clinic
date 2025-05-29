from rest_framework import serializers
from .models import EmployeeAddress, WorkSchedule, Employee
from user.models import User


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
            'home',
        ]


class EmployeeGetSerializer(serializers.ModelSerializer):
    address = EmployeeAddressSerializer(read_only=True)
    schedule = WorkScheduleSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = [
            'id',
            'user',
            'first_name',
            'last_name',
            'father_name',
            'mobile_phone',
            'home_phone',
            'birth_date',
            'email',
            'gender',
            'profession',
            'is_accepting_appointments',
            'schedule',
            'address',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class EmployeeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = [
            'id',
            'user',
            'first_name',
            'last_name',
            'father_name',
            'mobile_phone',
            'home_phone',
            'birth_date',
            'email',
            'gender',
            'profession',
            'is_accepting_appointments',
            'created_at',
            'updated_at',
        ]
