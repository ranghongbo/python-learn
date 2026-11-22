# day24_practice.py - request another site
import requests

resp = requests.get("https://www.bing.com")
print(resp.status_code)

resp.encoding = "utg-8"
print(resp.text[:100])