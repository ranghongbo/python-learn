#  day6.py - business card generator 

# collect info
name = input("your full name: ")
job = input("your job title: ")
city = input("which city: ")
years = int(input("how many years experience: "))
skill = input("your main skill: ")

# print card
print("----------------------")
print(f" {name}")
print(f" {job}")
print(f" based in {city}")
print(f" specialty: {skill}")
print(f" {years} years experience")
print("----------------------")