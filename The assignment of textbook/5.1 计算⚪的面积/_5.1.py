import math as m
while True:
    r = input('Please enter radius:')
    try:
        r = float(r)
    except:
        print('Error. The number you entered is not a real number. Please re-enter a number')
    else:
        def areas(x):
            s = m.pi*x*x
            return s
            
        print('The area of a circle is :',areas(r))
        break