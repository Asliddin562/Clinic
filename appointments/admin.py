# appointments/admin.py
from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'date', 'start_time', 'end_time', 'created_at')
    list_filter = ('date', 'doctor')
    search_fields = ('doctor__username', 'patient__first_name', 'patient__last_name')
    ordering = ('-date', 'start_time')
    readonly_fields = ('created_at', 'updated_at')

    autocomplete_fields = ['doctor', 'patient']

