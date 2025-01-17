#USB Shopper 

print('\"A girl heads to a computer shop to buy some USB sticks.')
print('She loves USB sticks and wants as many as she can get for £50.')
print('They are £6 each.\"')

print('How many USB sticks can she buy and how many pounds will she have left?')

#Number of USBS within a £50 Budget

budget = 50
price = 6 

calculation_1 = budget/price
number_of_usbs = int(calculation_1)

#Amount of Pounds Left
calculation_2 = number_of_usbs * price
remaining_pounds = budget - calculation_2

print('- The girl can buy', number_of_usbs, 'USB sticks within a £50 budget,', 'with', remaining_pounds, 'pounds remaining.')

