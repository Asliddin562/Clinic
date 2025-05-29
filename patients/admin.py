from django.contrib import admin
from .models import PatientAddress, MedicalHistory, Patient

@admin.register(PatientAddress)
class PatientAddressAdmin(admin.ModelAdmin):
    list_display = ('region', 'district', 'street', 'home')
    search_help_text = ('region', 'district', 'street')


@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ("diagnosis", "date")


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'phone', 'birth_date')
    search_fields = ('first_name', 'last_name', 'phone')
    list_filter = ('gender', 'birth_date')
    ordering = ('last_name', 'first_name')


