from django.db import models
from django.utils.translation import gettext_lazy as _


class PatientAddress(models.Model):
    region = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    home = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.district}, {self.street}, {self.home}"


class MedicalHistory(models.Model):
    diagnosis = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    image = models.ImageField(upload_to='medical_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.patient.first_name} {self.patient.last_name} - {self.diagnosis}"


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
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.OneToOneField(PatientAddress, on_delete=models.SET_NULL, null=True, blank=True)
    history = models.ForeignKey(MedicalHistory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.gender})"



