from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from services.models import *


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'title', 'order')
    list_display_links = ('title',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subtitle', 'price', 'category', 'is_home_page']


@admin.register(ImageService)
class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'service']


@admin.register(Characteristics)
class CharacteristicsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'value', 'service']


@admin.register(ProcedureCost)
class ProcedureCostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'service']



