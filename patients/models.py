from django.db import models
from django.utils.translation import gettext_lazy as _
from employees.models import Employee


class Patient(models.Model):
    GENDER_CHOICES = [
        ('male', _('Man')),
        ('female', _('Woman')),
    ]
    card_number = models.IntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile_phone1 = models.CharField(max_length=30)
    mobile_phone2 = models.CharField(max_length=30, null=True, blank=True)
    home_phone = models.CharField(max_length=30, null=True, blank=True)
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    extra_comment = models.TextField(null=True, blank=True)
    patient_recommendation = models.TextField(null=True, blank=True)
    future_appointment = models.DateField(null=True, blank=True)
    treated_doctors = models.ManyToManyField(Employee, blank=True, related_name='treated_doctor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.gender})"


class PatientAddress(models.Model):
    patient = models.OneToOneField(
        Patient, on_delete=models.SET_NULL, null=True, blank=True, related_name='address')
    region = models.CharField(max_length=30)
    district = models.CharField(max_length=30, null=True, blank=True)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=100, null=True, blank=True)
    apartment = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.district}, {self.apartment}"


class MedicalHistory(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.SET_NULL, null=True, blank=True, related_name="history")
    diagnosis = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    image = models.ImageField(upload_to='medical_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.patient.first_name} {self.patient.last_name} - {self.diagnosis}"



