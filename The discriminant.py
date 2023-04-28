
a=1.5
b=5.7
c=-3.3

import math 

isnagative = b**2 - 4*a*c
if isnagative <0:
    print("it's negative")

x1= (-b -math.sqrt(b**2 - 4*a*c)) / 2*a
x2= (-b +math.sqrt(b**2 - 4*a*c)) / 2*a

print("The roots are given by", x1,"and", x2 )