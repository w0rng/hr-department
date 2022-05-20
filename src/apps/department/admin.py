from apps.department import models
from django.contrib import admin


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "chief", "phone"]


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "department"]
