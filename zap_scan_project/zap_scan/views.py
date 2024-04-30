from django.http import JsonResponse
from django.shortcuts import render
from .models import Alert
from zapv2 import ZAPv2
import pandas as pd
from io import StringIO
import time

def run_scan(target_url):
    api_key = "j6l7bva0mji6q7qe1v02lll3d7"
    zap = ZAPv2(apikey=api_key)  # Initialize ZAP object here

    # Clear alerts before starting a new scan
    zap.core.delete_all_alerts()

    print("Starting spider scan...")
    spider_scan_id = zap.spider.scan(target_url)
    while int(zap.spider.status(spider_scan_id)) < 100:
        print("Spider progress: {}%".format(zap.spider.status(spider_scan_id)))
        time.sleep(5)
    print("Spider scan completed.")

    print("Starting active scan...")
    active_scan_id = zap.ascan.scan(target_url)
    while int(zap.ascan.status(active_scan_id)) < 100:
        print("Active scan progress: {}%".format(zap.ascan.status(active_scan_id)))
        time.sleep(5)
    print("Active scan completed.")

    alerts = zap.core.alerts()
    return alerts

def json_to_csv_and_save(alerts):
    if not alerts:
        return None  # Return None if no alerts are present

    df = pd.DataFrame(alerts)
    csv_data_str = df.to_csv(index=False)
    return csv_data_str

def scan_view(request):
    # View function for the scan page
    if request.method == 'POST':
        target_url = request.POST.get('url', '')
        if target_url:
            try:
                # Delete all existing Alert objects before running the scan
                Alert.objects.all().delete()

                alerts = run_scan(target_url)
                csv_data_str = json_to_csv_and_save(alerts)
                if csv_data_str is not None:
                    csv_data = StringIO(csv_data_str)
                    alert_objects = pd.read_csv(csv_data).to_dict('records')
                    Alert.objects.bulk_create([
                        Alert(
                            sourceid=row['sourceid'],
                            other=row['other'],
                            method=row['method'],
                            evidence=row['evidence'],
                            pluginId=row['pluginId'],  
                            cweid=row['cweid'],
                            confidence=row['confidence'],  
                            wascid=row['wascid'],
                            messageId=row['messageId'],  
                            inputVector=row['inputVector'],
                            url=row['url'],
                            reference=row['reference'],  
                            alert=row['alert'],
                            param=row['param'],
                            attack=row['attack'],
                            alertRef=row['alertRef'],
                            name=row['name'],
                            risk=row['risk'],
                            description=row['description'],
                            solution=row['solution'],
                        )
                        for row in alert_objects
                    ])
                 
                    # Calculate alert counts
                    low_count, medium_count, high_count, total_count = calculate_alert_counts(alerts)
                 
                    # Redirect to the result page with alert counts as URL parameters
                    return redirect('result_page', high_count=high_count, medium_count=medium_count, low_count=low_count, total_count=total_count)
                else:
                    return JsonResponse({'error': 'No alerts found'})
            except Exception as e:
                return JsonResponse({'error': str(e)})
        else:
            return JsonResponse({'error': 'URL parameter is missing'})
    return render(request, 'zap_scan/scan.html')


def result_page(request, high_count, medium_count, low_count, total_count):
    # View function for the result page
    return render(request, 'zap_scan/result_page.html', {
        'high_count': high_count,
        'medium_count': medium_count,
        'low_count': low_count,
        'total_count': total_count,
    })

def calculate_alert_counts(alerts):
    # Calculate counts for low, medium, high, and total alerts
    low_count = sum(1 for alert in alerts if alert['risk'] == 'Low')
    medium_count = sum(1 for alert in alerts if alert['risk'] == 'Medium')
    high_count = sum(1 for alert in alerts if alert['risk'] == 'High')
    total_count = len(alerts)
    return low_count, medium_count, high_count, total_count



