# day5.py - f-string: fill boxes into text
name = "ranghongbo"
city = "hanchuan"

# old way:glue with +
print("hello " + name + ", you are from " + city)

# new way:f-string
print(f"hello {name}, you are from {city}")

# braces can hold expressions, not just boxes
age = 23
score = 8
print(f"next year you are {age + 1 }")
print(f"after treatment score: {score - 1}")