# day19_paractice.py - loop until valid number
while True:
  try:
    score = int(input("enter score (0-10): "))
    print(f"score is {score}")
    break
  except:
    print("that iss not a number, try again")
