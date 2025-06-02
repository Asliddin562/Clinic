from django.db import models
from user.models import User
from django.utils.translation import gettext_lazy as _


class Profession(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"



class Employee(models.Model):
    GENDER_CHOICES = [
        ('male', _('Man')),
        ('female', _('Woman')),
    ]

    EARNING_TYPE_CHOICES = [
        ('fixed', _('Fixed')),
        ('percentage', _('Percentage'))
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employees")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30, null=True, blank=True)
    mobile_phone1 = models.CharField(max_length=20)
    mobile_phone2 = models.CharField(max_length=20, null=True, blank=True)
    home_phone = models.CharField(max_length=20, null=True, blank=True)
    birth_date = models.DateField()
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Man')
    profession = models.ManyToManyField(Profession, blank=True, related_name='employee')
    is_accepting_appointments = models.BooleanField(default=False)
    earning_type = models.CharField(max_length=10, choices=EARNING_TYPE_CHOICES, default='Fixed')
    commission_percentage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fixed_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_working = models.BooleanField(default=False)
    is_using_program = models.BooleanField(default=False)
    passport_id = models.CharField(max_length=20, null=True, blank=True)
    chair = models.CharField(max_length=20, null=True, blank=True)
    color_hex = models.CharField(max_length=20, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EmployeeAddress(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="address")
    region = models.CharField(max_length=20)
    district = models.CharField(max_length=20, null=True, blank=True)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=100, null=True, blank=True)
    apartment = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.employee} {self.district}, {self.apartment}"


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

