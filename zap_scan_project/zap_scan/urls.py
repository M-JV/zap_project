#zap_scan_project/zap_scan/urls.py

from django.urls import path
from .views import scan_view

urlpatterns = [
    path('scan/', scan_view, name='scan'),  # Define the URL pattern for the scan_view
    
]
