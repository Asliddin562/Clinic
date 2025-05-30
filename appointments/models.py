from django.db import models
from employees.models import Employee
from patients.models import Patient
from django.utils.translation import gettext_lazy as _

class Appointment(models.Model):
    APPOINTMENT_STATUS_CHOICES = [
        ('scheduled', _('Scheduled')),
        ('completed', _('Completed')),
        ('canceled', _('Canceled')),
        ('upcoming_task', _('Upcoming Task')),
        ('upcoming_visit', _('Upcoming Visit')),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments', null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=APPOINTMENT_STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient} {self.start_time}-{self.end_time} ({self.status})"
