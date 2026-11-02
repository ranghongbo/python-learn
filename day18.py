# day18.py - default parameter
def greet(name, msg="hello"):
    print(f"{msg} {name}")

greet("wang")
greet("li", "hi")

def calc(a, b):
    return a + b, a - b

s, d = calc(10, 3)
print(s)
print(d)