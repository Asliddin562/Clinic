from django.contrib import admin
from employees.models import Employee, EmployeeAddress, WorkSchedule

class WorkScheduleInline(admin.StackedInline):
    model = WorkSchedule
    can_delete = False
    verbose_name_plural = 'Work Schedule'
    fk_name = 'employee'


@admin.register(EmployeeAddress)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('region', 'district', 'street', 'home')
    search_fields = ('region', 'district', 'street')

# Employee uchun admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile_phone', 'email', 'profession', 'gender', 'created_at')
    list_filter = ('gender', 'profession', 'created_at', 'is_accepting_appointments')
    search_fields = ('first_name', 'last_name', 'mobile_phone', 'email', 'is_accepting_appointments')
    inlines = [WorkScheduleInline]  # Jadvalni birga ko‘rsatish
    readonly_fields = ('created_at', 'updated_at')




@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ('employee', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

