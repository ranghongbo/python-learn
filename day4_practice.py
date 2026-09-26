total = int(input("how many patients today? "))
therapists = int(input("how many therapists on duty? "))
print("each therapist gets " + str(total // therapists) + " patients")
print(str(total % therapists ) +" patients left over")