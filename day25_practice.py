# day25_practice.py
import requests

resp = requests.get("https://v1.hitokoto.cn")
resp.encoding = "utf-8"
data = resp.json()

print("sentence:", data["hitokoto"])
print("from:", data["from"])
print("who:", data["from_who"])
print("id:", data["id"])

import json

text = '{"user": {"name": "wang", "age": 23}}'
data = json.loads(text)

print(data)
print(data["user"])
print(data["user"]["name"])

print(text["user"])