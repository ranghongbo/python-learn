# day12.py - for loop with range
for i in range(5):
    print(i)

# day12.py - number each patient
patients = ["wang", "li", "zhang"]
for i in range(len(patients)):
   print(i,patients[i])
   
score = 9
if score >= 8:
    print("severe pain")
else:
    print("mild pain")
