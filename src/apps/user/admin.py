from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {"fields": ("first_name", "middle_name", "last_name", "email", "phone", "address", "photo")},
        ),
        (
            _("Permissions"),
            {
                "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions"),
            },
        ),
        ("Паспортные данные", {"fields": ("pasport_date", "pasport_department", "pasport_number")}),
        ("Служебная информация", {"fields": ("post",)}),
        (_("Important dates"), {"fields": ("last_login", "date_joined", "date_birth")}),
    )
