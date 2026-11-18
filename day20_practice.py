# day20_practice.py - asave my info and read back
with open("my_info.txt", "w", encoding="utf-8") as f:
    f.write("name: ranghongbo\n")
    f.write("age:23\n")
    f.write("job:rehab therapist\n")
    f.write("city:hanchuan\n")

with open("my_info.txt", "r", encoding="utf-8") as f:
    info = f.read()

print(info)