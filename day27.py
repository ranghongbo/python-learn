# day27.py
import json

data = {"name": "wang", "city": "汉川", "note": "青春有百花秋有月"}

with open("city.json", "w", encoding= "utf-8") as f:
    json. dump(data, f, ensure_ascii=False, indent=2)