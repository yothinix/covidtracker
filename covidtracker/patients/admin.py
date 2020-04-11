from django.contrib import admin

from patients.models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'email', 'is_positive', 'last_update']
    list_display_links = ['name']
    list_filter = ['is_positive', 'age']
    search_fields = ['name', 'email']
    ordering = ['id']
    list_per_page = 2


# admin.site.register(Patient, PatientAdmin)
