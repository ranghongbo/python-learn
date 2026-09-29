# day10.py - list of dictionaries

patients = [
   {"name": "wang", "part": "neck", "score": 8},
   {"name": "li", "part": "waist", "score": 6},
   {"name": "zhang", "part": "knee", "score": 9},
]
print(patients)

print(patients[1])
print(patients[1] ["name"])
print(patients[1] ["score"])

patients.append({"name": "zhao", "part": "shoulder", "score": 5})
print(len(patients))
print(patients[3] ["name"])