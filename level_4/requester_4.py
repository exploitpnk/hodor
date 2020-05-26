#!/usr/bin/python3
"""
Hodor - Hbtn project

Level 4: HTTP request with parameters, cookies and proxies

Usage: python3 requester_4.py [id]

Author: @exploitpnk
"""
import requests
import sys
import os
import time

if len(sys.argv) == 2:
    url = "http://158.69.76.135/level4.php"
    user_id = sys.argv[1]
    data = {
        "id": user_id,
        "holdthedoor": "Submit+Query",
        "key": "0"
        }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) Safari/537.36",
        "Cookie": "HoldTheDoor=0",
        "Referer": "http://158.69.76.135/level4.php"
        }
    proxies = {
      "http": "socks5://127.0.0.1:9050",
      "https": "socks5://127.0.0.1:9050"
      }
    for i in range(1, 99):
        os.system("service tor restart") # Restarting tor service to get a new identity
        time.sleep(45) # Wait 45 seconds while tor service is running completely
        print("[#] New IP:", requests.get("https://canihazip.com/s", proxies=proxies).text) # Checking what's is our new IP address
        response = requests.post(url=url, data=data, headers=headers, proxies=proxies)
        print("[#] Request", i, "sent: HTTP code:", response.status_code)
else:
    print("Usage: sudo python3", sys.argv[0], "[id]")
