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
        max_length=30,
        choices=APPOINTMENT_STATUS_CHOICES,
        default='pending'
    )
    reason = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    sms_notification = models.BooleanField(default=False)
    sms_text = models.TextField(null=True, blank=True)
    add_to_waiting_list = models.BooleanField(default=False)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='appointment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient} {self.start_time}-{self.end_time} ({self.status})"
