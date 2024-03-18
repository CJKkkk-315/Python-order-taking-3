#ACME book club that awards points to its customers
#Author: David Smith
#Date Created: 28/6/2021
#Assessment : Week2 Lab1
# Get the number of books purchased from the user.
number = int(input( 'Enter the number of books purchased: '))
#Determine points earned .
if number >= 1 and number <= 2:
    points = 5
elif number >= 3 and number <= 4:
    points = 15
elif number >=5 and number<= 6:
    points = 30
elif number >=7:
    points = 60
else:
    points = 0
#Display the number of points earned .
print('You have purchased', number, 'books.')
print('This earns you ', points,'points.')
