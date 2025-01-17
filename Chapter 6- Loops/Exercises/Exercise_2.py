# Exercise 2: Movie Tickets

print("Welcome to the Movie Theater! Please enter your age and pay the given amount for your ticket.")

while True:
    age = int(input("Enter your age: "))
    if age < 3:
        print("Your movie ticket is free of charge.")
        break
    elif 3 <= age < 12:
        print("Your movie ticket will cost you $10.")
        break
    elif age <= 12: 
        print("Your movie ticket will cost you $15.")
        break