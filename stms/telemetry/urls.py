from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('api/receive-data/', views.TelemetryDataAPIView.as_view(), name='receive_data'),
]