name = "pengxianya"
print(name[2])
print(name[9])
print(name[0:10])

patients = ["peng", "rang", "wang", "xu", "liu"]
print(patients[0:1])
print("peng" in patients)
print("rang" in patients)
print("xianya" in "pengxianya")

team = ["peng", "rang", "wang", "xu", "liu"]
who = input("who to check: ")
if who in team:
    print("found")
else:
    print("not found")
    print(who[0])
    print(who[-1])