from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from AML.models import *


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name',  'email', 'is_staff']
    list_display_links = ['id', 'username']
    ordering = ['-id']
    fieldsets = (
        (
            None, {
                'fields': ('username', 'password')
            }
        ),
        (
            ('Employee Information '), {
                'fields': (
                    'first_name', 'last_name', 'email', 'government_id', 'phone_number',
                    'employee_id', 'employment_date', 'department', 'work_status', 'usage'
                )
            }
        ),
        (
            ('Permissions'), {
                'fields': (
                    'is_active',
                )
            }
        ),
        (
            ('Important dates'), {
                'fields': (
                    'last_login', 'date_joined'
                )
            }
        ),
    )


admin.site.register(TwitterFollower)
