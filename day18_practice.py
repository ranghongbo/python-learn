# day18_practice.py - triage function
def triage(name, score):
    if score >= 8:
        level = "severe"
    elif score >= 4:
        level = "moderate"
    else:
        level = "mild"
    return name,level

n, l = triage("wang", 9)
print(n, l)

n, l = triage("li", 5)
print(n, l)

n, l = triage("zhang", 2)
print(n, l)
