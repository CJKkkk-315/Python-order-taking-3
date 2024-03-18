def function():
    # str variable accepted book name
    book_name = input("Please Enter the Name of the Book : ")
    # int variable accepted number of books
    num_of_copies = int(input('Please Enter the number of copies that you bought : '))
    # float variable accepted price of books
    price = float(input("Please Enter the price of each book : "))
    # calculate total price
    total_cost = num_of_copies*price
    # print total price
    print('Total cost of the books purchased is : ', total_cost)


if __name__ == '__main__':
    function()