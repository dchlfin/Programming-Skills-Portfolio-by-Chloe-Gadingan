# Exercise 7: Seeing the World

#Store the locations in a list. 
# Make sure the list is not in alphabetical order.
top_five = ['Switzerland', 'Iceland', 'Japan', 'Italy', 'Korea']

#Print your list in its original order. 
# Don’t worry about printing the list neatly,
# just print it as a raw Python list.
print(top_five)

#Use sorted() to print your list in alphabetical order 
# without modifying the actual list.
print(sorted(top_five))

#Show that your list is 
#still in its original order by printing it.
print(top_five)

#Use sorted() to print your list in 
# reverse alphabetical order without 
# changing the order of the original list.
print(sorted(top_five, reverse=True))

#Show that your list is still in 
# its original order by printing it again.
print(top_five)

#Use reverse() to change the order of your list. 
top_five.reverse()
# Print the list to show that its order has changed
print(top_five)
#Use reverse() to change the order of your list again. 
top_five.reverse()
# Print the list to show it’s back to its original order.
print(top_five)

# Use sort() to change your list so it’s stored in 
# alphabetical order.
top_five.sort()
# Print the list to show that its order has been changed.
print(top_five)

##print(sorted(top_five, reverse=True))

# Use sort() to change your list so it’s stored in 
# reverse alphabetical order. 
top_five.sort(reverse=True)
# Print the list to show that its order has changed.
print(top_five)
