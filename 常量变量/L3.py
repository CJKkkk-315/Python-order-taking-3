import tkinter
import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.geometry( "300x200")
window.resizable(width=False,height=False)
window.title( 'Salary Calculator ' )
hoursWorked = tk.StringVar()
payRate = tk.StringVar()
# define label and entry element
l1 = tk.Label(window, text="Hours worked: ", font=("Arial",10),fg="Black")
hoursWorked = tk.Entry(window,font=("Arial",11),textvariable=hoursWorked)
l2 = tk.Label(window, text="Pay Rate: ", font=("Arial", 10),fg="Black")
payRate = tk.Entry(window,font=("Arial",11),textvariable=payRate)
def calculate():
    # getting hour from entry and changing it to float then storing it to hours_work
    hours_work = float(hoursWorked.get())
    # getting rate from entry and changing it to float then storing it to pay_rate
    pay_rate = float(payRate.get())
    # multiplying h multiply r and storing it to pay
    pay = hours_work*pay_rate
    messagebox.showinfo('salary: ', pay)
details = tk.Button(window, text='Details' , width=10,command=calculate)
details.grid(row=0 , column=3)
# Placement of all labels/entry widgets
l1.place(x=20,y=40)
hoursWorked.place(x=120,y=40)
l2.place(x=20, y=100)
payRate.place(x=120,y=100)
details.place(x=20 ,y=150)
window.mainloop()
