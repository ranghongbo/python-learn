# day14_practice.py - ask and quit
while True:
    score = input("enter score (q to quit): ")
    if score == "q":
        break
    score = int(score)
    if score >= 8:
       print("severe pain")
    elif score >= 4:
        print("moderate pain")
    else:
        print("mild pain")