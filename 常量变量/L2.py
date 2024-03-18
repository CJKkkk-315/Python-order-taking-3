def function():
    # Declaration of the Named Constant
    CENTIMETERS_PER_INCH = 2.54
    INCHES_PER_FOOT = 12
    # user input
    feet = int(input('Enter feet : '))
    inches = float(input('Enter inches : '))
    # processing input
    totalInches = (INCHES_PER_FOOT * feet + inches)
    centimeter = (CENTIMETERS_PER_INCH * totalInches)
    # printing formatted output
    print(f'The total number of Centimeters : {centimeter:>15.2f}')


if __name__ == '__main__':
    function()
