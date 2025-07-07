from rest_framework import viewsets
from user.permissions import IsAdmin, IsDirector, IsDoctor
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.timezone import now
from collections import defaultdict
from datetime import datetime, timedelta, date as date_cls, time as time_cls
from .models import Appointment, Employee
from .serializers import AppointmentSerializer, AppointmentListSerializer
from .filters import AppointmentFilter
from .utils import get_duration_hours, get_color_by_percent, is_working_on_date

class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = AppointmentFilter
    permission_classes = [IsAdmin | IsDirector | IsDoctor | AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return AppointmentListSerializer
        return AppointmentSerializer

    def list(self, request, *args, **kwargs):
        today = now().date()
        date_str = request.query_params.get('date')
        start_time_str = request.query_params.get('start_time')
        end_time_str = request.query_params.get('end_time')
        employee_id_param = request.query_params.get('employee_id')
        profession_id_param = request.query_params.get('profession_id')
        range_param = request.query_params.get('range')
        minute_param = request.query_params.get('min')

        if date_str:
            try:
                date_to_filter = datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                date_to_filter = today
        else:
            date_to_filter = today

        filtered_appointments = Appointment.objects.all().filter(date=date_to_filter)
        if employee_id_param:
            filtered_appointments = filtered_appointments.filter(employee_id=employee_id_param)
        elif profession_id_param:
            filtered_appointments = filtered_appointments.filter(employee__profession__id=profession_id_param)

        if start_time_str:
            filtered_appointments = filtered_appointments.filter(end_time__gt=start_time_str)
        if end_time_str:
            filtered_appointments = filtered_appointments.filter(start_time__lt=end_time_str)

        serializer = self.get_serializer(filtered_appointments, many=True)

        calendar_stats_by_day = []
        if range_param:
            try:
                month_count = int(range_param.replace("month", ""))
            except ValueError:
                month_count = 1

            start_month = date_to_filter.replace(day=1)
            end_month = (start_month.month + month_count - 1) % 12 or 12
            end_year = start_month.year + ((start_month.month + month_count - 1) // 12)
            end_day = 28
            while True:
                try:
                    end_date = date_cls(end_year, end_month, end_day)
                    break
                except:
                    end_day -= 1

            start_time = datetime.strptime(start_time_str, "%H:%M").time() if start_time_str else None
            end_time = datetime.strptime(end_time_str, "%H:%M").time() if end_time_str else None
            minute = int(minute_param) if minute_param else None

            current = start_month
            while current <= end_date:
                daily_appointments = Appointment.objects.filter(date=current)
                if employee_id_param:
                    daily_appointments = daily_appointments.filter(employee_id=employee_id_param)
                elif profession_id_param:
                    daily_appointments = daily_appointments.filter(employee__profession__id=profession_id_param)

                if start_time and end_time:
                    daily_appointments = daily_appointments.filter(start_time__lt=end_time, end_time__gt=start_time)

                appointment_hours = defaultdict(float)
                employee_ids = set()
                for app in daily_appointments:
                    appointment_hours[app.employee_id] += get_duration_hours(app.start_time, app.end_time)
                    employee_ids.add(app.employee_id)

                if employee_id_param:
                    employees = Employee.objects.filter(id=employee_id_param)
                elif profession_id_param:
                    employees = Employee.objects.filter(profession__id=profession_id_param)
                else:
                    employees = Employee.objects.all()

                employees = employees.prefetch_related('schedule')

                percents = []
                available_slots = 0
                total_slots = 0

                for emp in employees:
                    try:
                        schedule = emp.schedule
                    except Employee.schedule.RelatedObjectDoesNotExist:
                        continue

                    if not is_working_on_date(schedule, current):
                        continue

                    eff_start = start_time if start_time else time_cls(9, 0)
                    eff_end = end_time if end_time else time_cls(23, 0)
                    total_minutes = (datetime.combine(current, eff_end) - datetime.combine(current, eff_start)).seconds / 60
                    total_hours = total_minutes / 60 if total_minutes > 0 else 1

                    if minute:
                        emp_apps = Appointment.objects.filter(employee=emp, date=current)
                        slot_time = datetime.combine(current, eff_start)
                        end_dt = datetime.combine(current, eff_end)

                        while slot_time + timedelta(minutes=minute) <= end_dt:
                            slot_end = slot_time + timedelta(minutes=minute)
                            conflict = emp_apps.filter(
                                start_time__lt=slot_end.time(),
                                end_time__gt=slot_time.time()
                            ).exists()
                            if not conflict:
                                available_slots += 1
                            total_slots += 1
                            slot_time = slot_time + timedelta(minutes=15)
                    else:
                        booked = appointment_hours.get(emp.id, 0)
                        percent = int((min(booked, total_hours) / total_hours) * 100)
                        percents.append(percent)

                if minute:
                    if total_slots:
                        avg_percent = int((1 - available_slots / total_slots) * 100)
                        color = get_color_by_percent(avg_percent)
                    else:
                        avg_percent = 0
                        color = "blue"
                elif percents:
                    avg_percent = int(sum(percents) / len(percents))
                    color = get_color_by_percent(avg_percent)
                else:
                    avg_percent = 0
                    color = "blue"

                calendar_stats_by_day.append({
                    "date": current.strftime('%Y-%m-%d'),
                    "average_percent": avg_percent,
                    "color": color
                })

                current += timedelta(days=1)

        return Response({
            "appointments": serializer.data,
            "calendar_stats_summary_by_day": calendar_stats_by_day
        })



# from rest_framework import viewsets
# from user.permissions import IsAdmin, IsDirector, IsDoctor
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend
# from django.utils.timezone import now
# from collections import defaultdict
# from datetime import datetime
# from .models import Appointment, Employee
# from .serializers import AppointmentSerializer
# from .filters import AppointmentFilter
# from .utils import get_duration_hours, get_color_by_percent, is_working_on_date
#
#
# class AppointmentViewSet(viewsets.ModelViewSet):
#     serializer_class = AppointmentSerializer
#     queryset = Appointment.objects.all()
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = AppointmentFilter
#     permission_classes = [IsAdmin | IsDirector | IsDoctor | AllowAny]
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#
#         # Parametrlarni olish
#         today = now().date()
#         date_str = request.query_params.get('date')
#
#         if date_str:
#             try:
#                 date_to_filter = datetime.strptime(date_str, '%Y-%m-%d').date()
#             except ValueError:
#                 date_to_filter = today
#         else:
#             date_to_filter = today
#
#         doctor_hours = defaultdict(float)
#         employee_ids_in_queryset = set()
#
#         for app in queryset:
#             duration = get_duration_hours(app.start_time, app.end_time)
#             doctor_hours[app.employee_id] += duration
#             employee_ids_in_queryset.add(app.employee_id)
#
#         # Agar aniq employee_id so‘rovda bo‘lsa, faqat o‘sha xodimni olaylik
#         employee_id_param = request.query_params.get('employee_id')
#         if employee_id_param:
#             employees = Employee.objects.filter(id=employee_id_param).prefetch_related('schedule')
#         else:
#             employees = Employee.objects.filter(id__in=employee_ids_in_queryset).prefetch_related('schedule')
#
#         percent_list = []
#
#         for emp in employees:
#             schedule = getattr(emp, 'schedule', None)
#             if not schedule or not is_working_on_date(schedule, date_to_filter):
#                 percent = 100
#             else:
#                 total_hours = 13
#                 booked = doctor_hours.get(emp.id, 0)
#                 percent = int((booked / total_hours) * 100)
#             percent_list.append(percent)
#
#         # Umumiy o‘rtacha foiz va rang
#         if percent_list:
#             avg_percent = int(sum(percent_list) / len(percent_list))
#             summary_color = get_color_by_percent(avg_percent)
#             calendar_stats_summary = {
#                 "average_percent": avg_percent,
#                 "color": summary_color
#             }
#         else:
#             calendar_stats_summary = None
#
#         return Response({
#             "appointments": serializer.data,
#             "calendar_stats_summary": calendar_stats_summary
#         })
