# Python Program Number Analysis tool
#Author: David Smith
# Date Created : 28/6/2021
#Assessment : Week2 Lab2
import turtle as w  #w is the reference variable
number = int(w.numinput('Input','Enter the number')) # User Input
# #Analysing the number
if number <=0:#
    output = 'The Number is Negative.'
elif number >0:
    output = 'The Number is positive.'
    if number%2==0:
        output=output+' and Even'
    else:
        output = output+' and Odd '
#printing the output
w.hideturtle()
w.write(output)
w.mainloop()   #Loop the output window
