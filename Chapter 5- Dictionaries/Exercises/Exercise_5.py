# Exercise 5: Pets

pets = [
    {"Dog:":"Dave"},
    {"Cat:":"Cami"},
    {"Fish:":"Felix"}
]

for pet in pets:
    for key,val in pet.items():
        print(f"{key} {val}")
        