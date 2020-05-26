#!/usr/bin/python3
"""
Hodor - Hbtn project

Level 1: HTTP request with parameters and cookies

Usage: python3 requester_1.py [id]

Author: @exploitpnk
"""
import requests
import sys

if len(sys.argv) == 2:
    url = "http://158.69.76.135/level1.php"
    user_id = sys.argv[1]
    data = {
        "id": user_id,
        "holdthedoor": "Submit+Query",
        "key": "0"
        }
    headers = {
        "Cookie": "HoldTheDoor=0"
        }
    for i in range(1, 1024):
        response = requests.post(url=url, data=data, headers=headers)
        print("[#] Request", i, "sent: HTTP code:", response.status_code)
else:
    print("Usage: python", sys.argv[0], "[id]")
