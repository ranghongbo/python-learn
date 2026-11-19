# day21.py - append to a file
with open("names.txt", "a", encoding="utf-8") as f:
    f.write("wang\n")

with open("names.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(lines)

for line in lines:
    print(line.strip())