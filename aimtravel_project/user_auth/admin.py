from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from aimtravel_project.user_auth.forms import SignUpForm, EditForm
from aimtravel_project.user_auth.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(auth_admin.UserAdmin):
    ordering = ('email',)
    list_display = ['email', 'date_joined', 'last_login', 'is_staff', 'is_superuser', 'is_active']
    list_filter = ('email', "is_staff", "is_superuser", "is_active")
    search_fields = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    add_form = SignUpForm
    form = EditForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions",
         {
             "fields": (
                 "is_active",
                 "is_staff",
                 "is_superuser",
                 "groups",
                 "user_permissions",
             ),
         },
         ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
