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
            ('Personal Information '), {
                'fields': (
                    'first_name', 'last_name', 'email', 'government_id', 'phone_number',
                    'date_of_birth', 'country_of_citizenship'
                )
            }
        ),
        (
            ('Residence Address'), {
                'fields': (
                    'address1', 'address2', 'address_city', 'address_zip_code', 'address_country'
                )
            }
        ),
        (
            ('Work Infomation'), {
                'fields': (
                    'company', 'company_field_of_business', 'company_state', 'company_country'
                )
            }
        ),
        (
            ('Additional Information'), {
                'fields': (
                    'sns_facebook', 'sns_instagram', 'sns_twitter', 'sns_google', 'sns_linkedin'
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
