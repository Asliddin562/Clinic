from rest_framework import serializers
from .models import EmployeeAddress, WorkSchedule, Employee
from user.models import User


class EmployeeAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAddress
        fields = [
            'id',
            'region',
            'district',
            'street',
            'home',
        ]


class WorkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSchedule
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']



class EmployeeSerializer(serializers.ModelSerializer):
    address = EmployeeAddressSerializer()
    schedule = WorkScheduleSerializer(required=False)  # WorkSchedule OneToOne
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

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
            'address',
            'gender',
            'profession',
            'is_accepting_appointments',
            'schedule',
            'created_at',
            'updated_at',
        ]

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        schedule_data = validated_data.pop('schedule', None)

        address = EmployeeAddress.objects.create(**address_data)
        employee = Employee.objects.create(address=address, **validated_data)

        if schedule_data:
            WorkSchedule.objects.create(employee=employee, **schedule_data)

        return employee

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        schedule_data = validated_data.pop('schedule', None)

        # Update Address
        if address_data:
            for attr, value in address_data.items():
                setattr(instance.address, attr, value)
            instance.address.save()

        # Update Employee fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update or create WorkSchedule
        if schedule_data:
            schedule, created = WorkSchedule.objects.get_or_create(employee=instance)
            for attr, value in schedule_data.items():
                setattr(schedule, attr, value)
            schedule.save()

        return instance
