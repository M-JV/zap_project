#!/usr/bin/env python
import time
import requests
from pprint import pprint
from zapv2 import ZAPv2

def run_scan(target_url):
    apiKey = 'oe3cpm86q5kd99s15iat8r4ukq'
    zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

    # Start the active scan using ZAP API
    scanID = zap.ascan.scan(target_url)
    
    # Wait for the scan to complete
    while True:
        status = zap.ascan.status(scanID)
        if status == '100':
            break
        elif status == 'does_not_exist':  # Handle case where scanID is invalid
            raise Exception('Scan ID does not exist')
        time.sleep(5)

    # Retrieve vulnerabilities found by the scanning
    alerts = zap.core.alerts(baseurl=target_url)
    return alerts

if __name__ == "__main__":
    target = 'https://public-firing-range.appspot.com'  # Example URL
    print('Active Scanning target {}'.format(target))
    try:
        alerts = run_scan(target)
        print('Active Scan completed')
        print('Hosts: {}'.format(', '.join(zap.core.hosts)))
        print('Alerts: ')
        pprint(alerts)
    except Exception as e:
        print(f"Error occurred: {e}")
