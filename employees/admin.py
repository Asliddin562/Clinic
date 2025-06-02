from django.contrib import admin
from employees.models import Employee, EmployeeAddress, WorkSchedule, Profession

class WorkScheduleInline(admin.StackedInline):
    model = WorkSchedule
    can_delete = False


class EmployeeAddressInline(admin.StackedInline):
    model = EmployeeAddress
    can_delete = False


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']


# Employee uchun admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile_phone1', 'gender', 'created_at')
    list_filter = ('gender', 'profession', 'created_at', 'is_accepting_appointments', 'is_using_program', 'is_working')
    search_fields = ('first_name', 'last_name', 'mobile_phone', 'is_accepting_appointments')
    inlines = [WorkScheduleInline, EmployeeAddressInline]  # Jadvalni birga ko‘rsatish
    readonly_fields = ('created_at', 'updated_at')


@admin.register(EmployeeAddress)
class EmployeeAddressAdmin(admin.ModelAdmin):
    list_display = ('employee', 'region', 'district', 'street', 'building', 'apartment')
    search_fields = ('region', 'district', 'street', 'building')


@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ('employee', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

