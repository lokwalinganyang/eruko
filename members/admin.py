from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # This controls what you see in the "List View"
    list_display = ('username', 'national_id', 'phone_number', 'savings_balance', 'is_staff')
    
    # This adds the custom fields to the "Edit User" page
    fieldsets = UserAdmin.fieldsets + (
        ('SACCO Details', {'fields': ('national_id', 'phone_number', 'savings_balance')}),
    )
    
    # This adds the custom fields to the "Create User" page
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('SACCO Details', {'fields': ('national_id', 'phone_number', 'savings_balance')}),
    )