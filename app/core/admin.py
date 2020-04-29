from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _ #translate python to string

from core import models

class UserAdmin(BaseUserAdmin):
    ''' modify the default admin to list custom user model'''
    ordering = ['id']
    list_display = ['email', 'name']

    #fieldsets control layout of admin add and change page
    fieldsets = (
    (None, {'fields': ('email', 'password')}),
    (_('Personal Info'), {'fields': ('name',)}),
    (
        _('Permissions'),
        {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }
    ),
    (_('Important dates'), {'fields': ('last_login',)}),
    )

    #fieldsets for adding new user by admin
    add_fieldsets = (
        (None, {
        'classes': ('wide',),
        'fields': ('email', 'password1', 'password2')
    }),
    )

admin.site.register(models.User,UserAdmin)     
