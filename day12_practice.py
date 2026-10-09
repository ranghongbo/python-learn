# plaintext
for i in range(4):
    print(i)

patients = ["wang", "li", "zhang", "xu"]
for i in range(len(patients)):
    print(f"{i} {patients[i]} - patient {i}")

records = [
    {"name": "wang", "score": 9},
    {"name": "li", "score": 5},
    {"name": "zhang", "score": 7},
]
for i in range(len(records)):
    if records[i] ["score"] >= 8:
        print(f"{records[i] ['name']} severe pain")
    else:
        print(f"{records[i] ['name']} mild pain")
