from django.contrib import admin

from check.models import TemperatureCheck


@admin.register(TemperatureCheck)
class TemperatureCheck(admin.ModelAdmin):
    list_display = ['patient', 'temperature', 'check_date']
