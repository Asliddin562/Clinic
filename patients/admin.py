from django.contrib import admin
from .models import PatientAddress, MedicalHistory, Patient

@admin.register(PatientAddress)
class PatientAddressAdmin(admin.ModelAdmin):
    list_display = ('patient', 'region', 'district', 'street', 'building', 'apartment')
    search_fields = ('region', 'district', 'street', 'building')

@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ("diagnosis", "date")


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'mobile_phone1', 'birth_date')
    search_fields = ('first_name', 'last_name', 'treated_doctors')
    list_filter = ('gender', 'birth_date')
    ordering = ('last_name', 'first_name')


