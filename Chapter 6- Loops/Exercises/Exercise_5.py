# Exercise 5: No Pastrami
sandwich_orders = ["Pastrami Sandwich", "Chicken Caesar Sandwich", "Pastrami Sandwich", "Tuna Sandwich", "Pastrami Sandwich", "Egg and Turkey Ham Sandwich"]
finished_sandwiches = []

print("The deli has run out of pastrami.\n")

while "Pastrami Sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami Sandwich")
    continue

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"Order for {current_sandwich} is ready!")

print(f'Orders for {finished_sandwiches} have been made.')
