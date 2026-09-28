my_patient = {"name" : "ranghongbo", "part" : "foot", "score" : 12, "treatment method" : "massage"}
print(my_patient)
print(f"{my_patient['name']} has {my_patient['part']} pain, score {my_patient['score']}")
my_patient["score"] = 11
print(f"after treatment, it is {my_patient['score']} ")