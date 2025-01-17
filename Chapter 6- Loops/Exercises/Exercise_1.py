# Exercise 1: Pizza Toppings

print("Enter as many pizza toppings as you want. When you're done, enter 'quit'.")

while True:
    userInput = input("Enter a topping: ")
    if userInput == "quit":
        print("Thank you! Enjoy your pizza.")
        break
    print(f"Adding {userInput} to your pizza...")