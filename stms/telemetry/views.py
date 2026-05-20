from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import TelemetryData, TelemetryDevices

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Telemetry App!")

@csrf_exempt
def receive_data_v01(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print("Received Data:", data)
        return JsonResponse({"message": "Data received successfully"})
    return JsonResponse({"error": "Invalid request"})

class TelemetryDataAPIView(APIView):

    """
    API endpoint to receive telemetry data from devices.
    """
    
    def post(self, request):
        data = request.data
        try:
            device = get_object_or_404(TelemetryDevices, id=data.get("device_id"))
            
            TelemetryData.objects.create(
                device=device,
                temperature=data.get("temperature"),
                pressure=data.get("pressure"),
                humidity=data.get("humidity"),
                latitude=data.get("latitude"),
                longitude=data.get("longitude"),
                battery_level=data.get("battery_level"),
            )
            
            print("Received Data:", data)
            
            return JsonResponse({"message": "Data received successfully"})
        
        except Exception as e:
            print("Error:", e)
            return JsonResponse({"error": "Failed to receive data"})

