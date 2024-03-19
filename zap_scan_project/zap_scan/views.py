from django.shortcuts import render
from django.http import JsonResponse
from zapv2 import ZAPv2
import time

def run_scan(target_url):
    api_key = "n8u0gb8krmkokc7du1vc0gbg2l"
    zap = ZAPv2(apikey=api_key)

    print("Starting spider scan...")
    scan_id = zap.spider.scan(target_url)
    while int(zap.spider.status(scan_id)) < 100:
        print("Spider progress: {}%".format(zap.spider.status(scan_id)))
        time.sleep(5)
    print("Spider scan completed.")

    print("Starting active scan...")
    scan_id = zap.ascan.scan(target_url)
    while int(zap.ascan.status(scan_id)) < 100:
        print("Active scan progress: {}%".format(zap.ascan.status(scan_id)))
        time.sleep(5)
    print("Active scan completed.")

    alerts = zap.core.alerts()
    return alerts

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
