# zap_scan/urls.py

from django.urls import path
from .views import scan_view, result_page

urlpatterns = [
    path('scan/', scan_view, name='scan'),  # Define the URL pattern for the scan_view
    path('result/', result_page, name='result_page'),
]
