from django.contrib import admin
from .models import TelemetryDevices, TelemetryData

# Register your models here.

@admin.register(TelemetryDevices)
class TelemetryDevicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name',)

@admin.register(TelemetryData)
class TelemetryDataAdmin(admin.ModelAdmin):
    list_display = ('device', 'timestamp', 'temperature', 'pressure', 'humidity')
    list_filter = ('device', 'timestamp')
    search_fields = ('device__name',)
