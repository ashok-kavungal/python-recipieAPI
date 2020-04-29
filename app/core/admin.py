from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models

class UserAdmin(BaseUserAdmin):
    ''' modify the default admin to list custom user model'''
    ordering = ['id']
    list_display = ['email', 'name']

admin.site.register(models.User,UserAdmin)     
