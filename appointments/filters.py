import django_filters
from .models import Appointment

class AppointmentFilter(django_filters.FilterSet):
    employee_id = django_filters.NumberFilter(field_name='employee__id')
    date = django_filters.DateFilter(field_name='date')
    start_time = django_filters.TimeFilter(field_name='start_time', lookup_expr='gte')
    end_time = django_filters.TimeFilter(field_name='end_time', lookup_expr='lte')
    profession_id = django_filters.NumberFilter(method='filter_by_profession')

    def filter_by_profession(self, queryset, name, value):
        return queryset.filter(employee__profession__id=value)

    class Meta:
        model = Appointment
        fields = ['employee_id', 'date', 'start_time', 'end_time', 'profession_id']
