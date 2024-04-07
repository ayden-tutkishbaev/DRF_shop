from django.contrib import admin
from common.models import *


@admin.register(Media)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'file_type']
    search_fields = ['file_type']
    list_filter = ['file_type']


@admin.register(CommonSettings)
class CommonSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'main_phone_number']


