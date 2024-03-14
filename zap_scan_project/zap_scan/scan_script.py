import requests
import time
from zapv2 import ZAPv2

def run_scan(target_url, api_key):
    # Perform the GET request using curl command to initiate the scan
    scan_url = f"http://localhost:8080/JSON/ascan/action/scan/?url={target_url}&apikey={api_key}"  # Include the API key in the URL
    response = requests.get(scan_url)
    if response.status_code != 200:
        raise Exception(f"Failed to initiate scan: {response.text}")

    # Initialize ZAP API connection
    zap = ZAPv2(apikey='71o2d4a4miu88v4pkgt3mcbutv', proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

    # Wait for the scan to complete
    while True:
        status = zap.ascan.status(scan_id)
        if status == '100':
            break
        elif status == 'does_not_exist':
            raise Exception('Scan ID does not exist')
        time.sleep(5)

    # Retrieve vulnerabilities found by the scanning
    alerts = zap.core.alerts(baseurl=target_url)
    return alerts
