# day5_practice.py - intake with f-string
name = input(" what is your name? ")
part = input(" where does it hurt? ")
score = int(input("rate your pain 0 to 10: "))
print(f"hello { name }, your {part } pain score is {score}")
print(f"after treatment it will be { score - 1 }")