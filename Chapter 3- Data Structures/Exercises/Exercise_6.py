# Exercise 6: Shrinking Guest List
dinner_guests = ['Ms. Leopoldo,', 'Ms. Alcorin,', 'Mr. Baltazar,']
print('Dear', dinner_guests[0], 'you are cordially invited to dine with me',
      'on Friday, November 8, 2024, at 7:00PM in La Brioche Restaurant, Galleria Mall, Abu Dhabi.',
      'Please arrive in formal attire.',
      'Thank you and I look forward to spending the evening with you. Love, Chloe Gadingan')

print('Dear', dinner_guests[1], 'you are cordially invited to dine with me',
      'on Friday, November 8, 2024, at 7:00PM in La Brioche Restaurant, Galleria Mall, Abu Dhabi.',
      'Please arrive in formal attire.',
      'Thank you and I look forward to spending the evening with you. Love, Chloe Gadingan')

print('Dear', dinner_guests[2], 'you are cordially invited to dine with me',
      'on Friday, November 8, 2024, at 7:00PM in La Brioche Restaurant, Galleria Mall, Abu Dhabi.',
      'Please arrive in formal attire.',
      'Thank you and I look forward to spending the evening with you. Love, Chloe Gadingan')


#Unavailable Guest
print('Unfortunately, Mr. Baltazar will be not available for dinner on November 8, 2024.')

#Modified Guest List
dinner_guests = ['Ms. Leopoldo,', 'Ms. Alcorin,', 'Ms. Cariño,']
print('Dear', dinner_guests[0], 'you are cordially invited to dine with me',
      'on Friday, November 8, 2024, at 7:00PM in La Brioche Restaurant, Galleria Mall, Abu Dhabi.',
      'Please arrive in formal attire.',
      'Thank you and I look forward to spending the evening with you. Love, Chloe Gadingan') 

print('Dear', dinner_guests[1], 'you are cordially invited to dine with me',
      'on Friday, November 8, 2024, at 7:00PM in La Brioche Restaurant, Galleria Mall, Abu Dhabi.',
      'Please arrive in formal attire.',
      'Thank you and I look forward to spending the evening with you. Love, Chloe Gadingan')

print('Dear', dinner_guests[2], 'you are cordially invited to dine with me',
      'on Friday, November 8, 2024, at 7:00PM in La Brioche Restaurant, Galleria Mall, Abu Dhabi.',
      'Please arrive in formal attire.',
      'Thank you and I look forward to spending the evening with you. Love, Chloe Gadingan')

#Two Guests Only
print('You can only invite two guests for dinner.')

print('Dear', (dinner_guests.pop(2)), 'I may have initially invited you to dinner,',
      'but unfortunately I must limit the number of guests.', 
      'I apologize for the cancelation. I would love to have your presence some other time!',
      'Thank you for understanding.',
      'Sincerely, Chloe Gadingan')

print('Dear', dinner_guests[0], 'I am glad to inform you that you are still invited to dinner',
      'on Friday evening, November 8, 2024.',
      'Thank you and I happily anticipate your presence by then.')

print('Dear', dinner_guests[1], 'I am glad to inform you that you are still invited to dinner',
      'on Friday evening, November 8, 2024.',
      'Thank you and I happily anticipate your presence by then.')


del dinner_guests[-2:]
print(dinner_guests)
