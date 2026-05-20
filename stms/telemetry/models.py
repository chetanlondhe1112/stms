from django.db import models

class TelemetryDevices(models.Model):
    """
    Model representing a telemetry device.
    """
    
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name

# Create your models here.
class TelemetryData(models.Model):
    """
    Model representing telemetry data received from devices.
    """
    
    device=models.ForeignKey(TelemetryDevices, on_delete=models.CASCADE, related_name='telemetry_data')
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    battery_level = models.FloatField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.device.name} - {self.timestamp}"
    