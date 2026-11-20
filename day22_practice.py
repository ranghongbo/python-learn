# day22_practice.py - random patient and score
import random

patients = ["wang", "li", "zhang"]
pick = random.choice(patients)
score = random.randint(0,10)

print(f"patient: {pick}, score: {score}")
