from django.db import models
from user.models import User
from django.utils.translation import gettext_lazy as _


class Employee(models.Model):
    GENDER_CHOICES = [
        ('male', 'Man'),
        ('female', 'Woman'),
    ]

    PROFESSION_CHOICES = [
        ('director', _('Director')),  # Rahbariyat
        ('admin', _('Administrator')),  # Administrator
        ('manager', _('Manager')),  # Menejer
        ('accountant', _('Accountant')),  # Buxgalter
        ('receptionist', _('Receptionist')),  # Qabulxonachi
        ('doctor', _('Doctor')),  # Umumiy shifokor
        ('dentist', _('Dentist')),  # Stomatolog
        ('pediatrician', _('Pediatrician')),  # Pediatr
        ('cardiologist', _('Cardiologist')),  # Kardiolog
        ('neurologist', _('Neurologist')),  # Neyrolog
        ('surgeon', _('Surgeon')),  # Jarroh
        ('gynecologist', _('Gynecologist')),  # Ginekolog
        ('dermatologist', _('Dermatologist')),  # Dermatolog
        ('psychiatrist', _('Psychiatrist')),  # Psixiatr
        ('therapist', _('Therapist')),  # Terapevt
        ('nurse', _('Nurse')),  # Hamshira
        ('pharmacist', _('Pharmacist')),  # Farmatsevt
        ('assistant', _('Assistant')),  # Assistent
        ('guard', _('Guard')),  # Qorovul
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30, null=True, blank=True)
    mobile_phone = models.CharField(max_length=20)
    home_phone = models.CharField(max_length=20, null=True, blank=True)
    birth_date = models.DateField()
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    profession = models.CharField(max_length=50, choices=PROFESSION_CHOICES, blank=True, null=True)
    is_accepting_appointments = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EmployeeAddress(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="address")
    region = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    home = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.employee} {self.district}, {self.home}"


class WorkSchedule(models.Model):
    employee = models.OneToOneField('Employee', on_delete=models.CASCADE, related_name='schedule')
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee} ish jadvali"

