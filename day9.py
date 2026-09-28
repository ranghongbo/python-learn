# day9.py - dictionary

patient = {"name": "wang", "part": "neck", "score": 8}
print(patient)
print(patient["part"])

patient["score"] = 7
patient["age"] = 45
print(patient)
print(f"{patient['name']} has {patient['part']} pain, score {patient['score']}")