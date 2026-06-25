from django.contrib import admin
from .models import Companies, Departments, Users, Employees, EmployeeProject

# Register your models here.

admin.site.register(Companies)
admin.site.register(Departments)
admin.site.register(Employees)
admin.site.register(Users)
admin.site.register(EmployeeProject)