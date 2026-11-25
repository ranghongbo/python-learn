# day26.py
import json
data = {"name": "wang","score": 8,"level": "severe"}

with open("user.json","w",encoding="utf-8") as f:
    json.dump(data,f)

print("done")