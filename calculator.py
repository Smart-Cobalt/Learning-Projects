import math
import sys
def roundNum():
    x = float(input("Number to round: "))
    y = int(input("Decimals to round to: "))
    output = round(x, y)
    print(output)
    calculate()
def end():
    print('Have a nice day!')
    sys.exit()
def addition():
    x = float(input('First number:    '))
    y = float(input('Second number:    '))
    output = x+y
    print (output)
    calculate()
def subtraction():
    x = float(input('First number:    '))
    y = float(input('Subtract this number:    '))
    output = x-y
    print (output)
    calculate()
def multiplication():
     x = float(input('First number:    '))
     y = float(input('Multiply  by this number:    '))
     output = x*y
     print (output)
     calculate()
def division():
    x = float(input('First number:    '))
    y = float(input('Divide  by this number:    '))
    if y == 0:
        print('Stop it you moron')
        calculate()
    else:
        output = x/y
        print (output)
        calculate()
def slope():
    print('First, the first equation:    ')
    m1 = float(input('Slope:    '))
    b1 = float(input('Y-Intercept:     '))
    print('Now, the second equation:    ')
    m2 = float(input('Slope:    '))
    b2 = float(input('Y-Intercept:     '))
    if m1 == m2:
        print('infinite intersections or parralell lines.')
    else:
        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
        print(f"These lines intersect at: x = {x}, y = {y}")
    calculate()
def exponent():
     x = float(input('Number:    '))
     y = float(input('To the power of:    '))
     output = x**y
     print (f"{output:,}")
     calculate()
def squareRoot():
    x = float(input('Get the square root of:    '))
    if x >= 0:
        print(math.sqrt(x))
        calculate()
    else:
        print('Stop it you moron, its gotta be positive!')
        squareRoot()
def percent():
    x = float(input('Input the number to find the percent of:    '))
    y = float(input('What percent? Do not add %.   '))
    output = x * (y/100)
    print(output)
    calculate()

def calculate():    
    type = input('Addition, Subtraction, Multiplication, Division, Slope, Exit, Exponent, Square Root, Percent, Round:    ').strip().lower()
    if type == 'addition' :
        addition()
    elif type == 'subtraction': 
        subtraction()
    elif type == 'multiplication': 
        multiplication()
    elif type == 'division' :
        division()
    elif type == 'slope' :
        slope()
    elif type == 'exit' :
        end()
    elif type == 'exponent':
        exponent()
    elif type == 'square root':
        squareRoot()
    elif type == 'square toot':
        print('Nice Typo!')
        calculate()
    elif type == 'percent':
        percent()
    elif type == 'round':
        roundNum()
    else:
        print('Invalid Option')
        calculate()
        
calculate()

