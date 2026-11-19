# day21_practice.py - save patients and read back

with open("patients.txt", "a", encoding="utf-8") as f:
   f.write("wang\n")
   f.write("li\n")
   f.write("zhang\n")

with open("patients.txt", "r", encoding="utf-8") as f:
   patients = f.readlines()

for p in patients:
   print(p.strip())