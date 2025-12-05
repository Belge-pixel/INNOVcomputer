from django.contrib import admin
from .models import StaffProfile


class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'position')
    search_fields = ('user__username', 'phone_number', 'position')
    
admin.site.register(StaffProfile, StaffAdmin)
