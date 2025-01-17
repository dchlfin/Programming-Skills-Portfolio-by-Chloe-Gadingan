# Exercise 4: Deli 

sandwich_orders = ["Chicken Caesar Sandwich", "Tuna Sandwich", "Egg and Turkey Ham Sandwich"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"Order for {current_sandwich} is ready!")

print(f'Orders for {finished_sandwiches} have been made.')






