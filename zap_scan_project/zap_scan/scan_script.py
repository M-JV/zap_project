from django.shortcuts import render
from django.http import JsonResponse
from .scan_script import run_scan

def scan_view(request):
    if request.method == 'POST':
        target_url = request.POST.get('url', '')
        if target_url:
            try:
                alerts = run_scan(target_url)
                return JsonResponse({'alerts': alerts})
            except Exception as e:
                return JsonResponse({'error': str(e)})
        else:
            return JsonResponse({'error': 'URL parameter is missing'})
    return render(request, 'zap_scan/scan.html')
