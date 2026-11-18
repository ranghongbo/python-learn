# day20.py - write to a file
with open("note.txt", "w", encoding="utf-8") as f:
    f.write("hello hongbo\n")
    f.write("this is day20\n")

with open("note.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)
