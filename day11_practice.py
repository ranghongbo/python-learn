patients = [
    {"name": "rang", "part": "knee", "score": 4},
    {"name": "peng", "part": "neck", "score": 2},
    {"name": "xu", "part": "waist", "score": 6},
]
for patie in patients:
     print(patie)
     print(f"{patie['name']} has {patie['part']} pain, score {patie['score']}")
