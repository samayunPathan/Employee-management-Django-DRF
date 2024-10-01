from django.contrib import admin
from employee.models import Department,Achievement,Employee,AchievementEmployee

# Register your models here.

admin.site.register(Department)
admin.site.register(Achievement)
admin.site.register(Employee)
admin.site.register(AchievementEmployee)
