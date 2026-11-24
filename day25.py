# day25.py - json basics
import json

text = '{"name": "wang","score": 8, "level": "severe"}'
data = json.loads(text)

print(data)
print(data["name"])
print(data["score"])

import requests

resp = requests.get("https://api.github.com/users/ranghongbo")
data = resp.json()

print(resp.status_code)
print(type(data))
print(data["login"])
print(data["public_repos"])