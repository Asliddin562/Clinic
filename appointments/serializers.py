from rest_framework import serializers
from patients.models import Patient, PatientAddress
from .models import Appointment
from patients.serializers import CreatePatientSerializer, PatientAddressSerializer
from employees.models import Employee
from datetime import datetime, timedelta, time
from django.utils.translation import gettext_lazy as _




class AppointmentSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.filter(is_accepting_appointments=True)
    )

    class Meta:
        model = Appointment
        fields = [
            'id',
            'employee',
            'patient',
            'date',
            'start_time',
            'end_time',
            'status',
            'reason',
            'comment',
            'sms_notification',
            'sms_text',
            'add_to_waiting_list',
            'created_by',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_by', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user.employees
        return super().create(validated_data)

    def validate(self, attrs):
        employee = attrs['employee']
        date = attrs['date']
        start_time = attrs['start_time']
        end_time = attrs['end_time']

        now = datetime.now()  # hozirgi sana + vaqt
        appointment_datetime = datetime.combine(date, start_time)

        #  O‘tgan vaqtga zayavka bo‘lmasin (bugungi kun lekin vaqt o‘tgan bo‘lsa ham)
        if appointment_datetime <= now:
            raise serializers.ValidationError(_("Cannot register for a past date and time."))

        # 1 oydan keyingi sana bo‘lmasin
        if date > now.date() + timedelta(days=60):
            raise serializers.ValidationError(_("You can only book within the next 30 days."))

        # Ish vaqti oraliqlari
        morning_start = time(9, 0)
        morning_end = time(13, 0)
        afternoon_start = time(14, 0)
        afternoon_end = time(23, 0)

        valid_morning = morning_start <= start_time < morning_end and morning_start < end_time <= morning_end
        valid_afternoon = afternoon_start <= start_time < afternoon_end and afternoon_start < end_time <= afternoon_end

        if not (valid_morning or valid_afternoon):
            raise serializers.ValidationError(_("Appointments can only be booked between 09:00–13:00 or 14:00–23:00."))

        # Shu vaqtda boshqa zayavka yo‘qligini tekshir
        overlapping_appointments = Appointment.objects.filter(
            employee=employee,
            date=date,
            start_time__lt=end_time,
            end_time__gt=start_time
        ).exclude(id=self.instance.id if self.instance else None)

        if overlapping_appointments.exists():
            raise serializers.ValidationError(_("This time slot is already booked."))

        # Doktor bu kuni ishlaydimi?
        weekday = date.weekday()  # 0 - Dushanba, ..., 6 - Yakshanba

        day_map = {
            0: 'monday',
            1: 'tuesday',
            2: 'wednesday',
            3: 'thursday',
            4: 'friday',
            5: 'saturday',
            6: 'sunday',
        }

        # Ish kunini tekshirish uchun:
        work_schedule = employee.schedule  # bitta WorkSchedule obyekti
        day_field = day_map[weekday]

        if not getattr(work_schedule, day_field):
            raise serializers.ValidationError(_("The doctor does not work on this day."))

        return attrs


class PatientShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'id',
            'first_name',
            'last_name',
            'father_name',
            'birth_date',
            'mobile_phone1',
            'comment'
        ]

class EmployeeShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'first_name',
            'last_name',
            'father_name'
        ]

class AppointmentListSerializer(serializers.ModelSerializer):
    employee = EmployeeShortSerializer(read_only=True)
    patient = PatientShortSerializer(read_only=True)
    class Meta:
        model = Appointment
        fields = [
            'id',
            'patient',
            'employee',
            'date',
            'start_time',
            'end_time',
            'status',
            'comment'
        ]

