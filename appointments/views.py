from rest_framework import viewsets
from user.permissions import IsAdmin, IsDirector, IsDoctor
from  rest_framework.permissions import AllowAny
from .models import Appointment, Employee
from .serializers import AppointmentSerializer, AppointmentListSerializer
from rest_framework.response import Response
from django.db.models import Count, Case, When
from datetime import date as date_cls


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('-created_at')
    serializer_class = AppointmentSerializer
    permission_classes = [IsAdmin|IsDirector|IsDoctor|AllowAny]



class DoctorAppointmentsViewSet(viewsets.ViewSet):
    permission_classes = [IsDirector|AllowAny]

    def list(self, request):
        # So‘rovdan date va employee_id ni olish
        requested_date = request.query_params.get('date')
        employee_id = request.query_params.get('employee_id')

        # Sana bo‘lmasa bugungi sanani o‘rnatamiz
        if requested_date:
            try:
                requested_date = date_cls.fromisoformat(requested_date)
            except ValueError:
                return Response({"detail": "Sana noto‘g‘ri formatda. YYYY-MM-DD formatida bering."}, status=400)
        else:
            requested_date = date_cls.today()

        # Agar employee_id berilsa, faqat shu employee va sana bo‘yicha appointmentlar
        if employee_id:
            appointments = Appointment.objects.filter(employee_id=employee_id, date=requested_date).order_by('-date', '-start_time')
            serializer = AppointmentListSerializer(appointments, many=True)
            return Response(serializer.data)

        # Aks holda, barcha employee lar uchun shu sana bo‘yicha appointmentlar
        # Avval employee ga tegishli appointmentlar sonini hisoblaymiz shu sana bo‘yicha
        employee_appointments_count = Appointment.objects.filter(date=requested_date) \
            .values('employee_id') \
            .annotate(appointment_count=Count('id')) \
            .order_by('-appointment_count')

        employee_ids_ordered = [item['employee_id'] for item in employee_appointments_count]

        # Tartibni saqlab qolish uchun Case ishlatamiz
        preserved_order = Case(*[When(employee_id=emp_id, then=pos) for pos, emp_id in enumerate(employee_ids_ordered)])

        appointments = Appointment.objects.filter(date=requested_date, employee_id__in=employee_ids_ordered) \
            .order_by(preserved_order, '-date', '-start_time')

        serializer = AppointmentListSerializer(appointments, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"detail": "Doktor topilmadi."}, status=404)

        appointments = Appointment.objects.filter(employee=employee).order_by('-date', '-start_time')
        serializer = AppointmentListSerializer(appointments, many=True)
        return Response(serializer.data)