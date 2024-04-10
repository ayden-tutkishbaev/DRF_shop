from django.contrib import admin

from clinics.models import *


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'requirements']
    search_fields = ['title', 'requirements', 'responsibilities', 'conditions']
