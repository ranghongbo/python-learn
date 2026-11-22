# day24.py - requests get
import requests

resp = requests.get("https://www.baidu.com")
print(resp.status_code)

resp.encoding = "utf-8"
print(resp.text)