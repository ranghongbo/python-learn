# day17.py - functions
def greet():
    print("hello wang")

greet()
greet()

# day17.py - function with parameter

def greet(name):
    print("hello " + name)

greet("wang")
greet("li")
greet("peng")

def add(a, b):
    return a + b

result = add(3, 5)
print(result)
