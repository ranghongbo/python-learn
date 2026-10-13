# day16.py - string methaods
sentence = "wang li zhang xu"
names = sentence.split()
print(names)

line = input("enter names: ")
names = line.split()
print(names)

messy = " wang "
print(messy)
clean = messy.strip()
print(clean)

msg = "hello world"
print(msg.replace("world", "python"))

team = ["wang", "xu", "li"]
team.sort()
print(team)

team.remove("li")
print(team)

last = team.pop()
print(last)
print(team)