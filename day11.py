# day11.py - for loop
patients = ["wang", "li", "zhang"]
for p in patients:
    print(p)


# day11.py - for loop over patient recoords
patients = [
    {"name": "wang", "part": "neck", "score": 8},
    {"name": "li", "part": "waist", "score": 6},
    {"name": "zhang", "part": "knee", "score": 9},
]
for p in patients:
    print(p)
    print(f"{p['name']} has {p['part']} pain, score {p['score']}")