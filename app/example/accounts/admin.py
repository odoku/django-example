# -*- coding: utf-8 -*-

from django.contrib.admin import ModelAdmin, register
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Administrator


@register(Administrator)
class AdministratorAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {
            'fields': [
                'email',
                'password',
                'is_active',
            ]
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ['email', 'password1', 'password2']
        }),
    )

    list_display = (
        'pk',
        'email',
        'is_active',
        'created_at',
        'modified_at',
    )
    ordering = []
    list_filter = tuple()
