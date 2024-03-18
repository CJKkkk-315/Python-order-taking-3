name = input('Customers Name:')
number = int(input('Number of items the customer purchased:'))
price = float(input('The item price:'))

G_payment = price * number
tax = G_payment * 0.1
N_payment = G_payment + tax

print("""
Dear {},
You have purchased {} items, and the item price = ${:.2f}
Based on that, the Gross payment = ${:.2f} and the GST = ${:.3f}
The Net payment you have to pay = ${:.3f}
Please let me know if you have any question.
With best regards,Yuanzhen Fu
""".format(name,number,price,G_payment,tax,N_payment))
