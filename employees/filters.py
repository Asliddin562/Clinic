import django_filters
from employees.models import Employee

class EmployeeFilter(django_filters.FilterSet):
    profession_id = django_filters.NumberFilter(field_name='profession__id')

    class Meta:
        model = Employee
        fields = ['profession_id']
