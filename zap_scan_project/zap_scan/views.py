from django.shortcuts import render
from django.http import JsonResponse
from .scan_script import run_scan

def scan_view(request):
    if request.method == 'GET':
        target_url = request.GET.get('url', '')
        if target_url:
            try:
                api_key = '71o2d4a4miu88v4pkgt3mcbutv'  # Replace this with your actual API key
                print("Using API Key:", api_key)  # Debug print
                alerts = run_scan(target_url, api_key)  # Pass the API key to run_scan
                return JsonResponse({'alerts': alerts})
            except Exception as e:
                return JsonResponse({'error': str(e)})
        else:
            return JsonResponse({'error': 'URL parameter is missing'}, status=400)
    return render(request, 'zap_scan/scan.html')
