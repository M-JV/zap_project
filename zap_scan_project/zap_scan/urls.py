#zap_scan_project/zap_scan/urls.py

from django.urls import path
from zap_scan.views import scan_view, chrome_scan_view
from report.views import results

urlpatterns = [
    path('scan/', scan_view, name='scan'),  # Define the URL pattern for the scan_view
    path('report/', results, name='report'),  # Define the URL pattern for the report view
     path('chrome_scan/', chrome_scan_view, name='chrome_scan'),  
]
