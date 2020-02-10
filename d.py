##Flux from absolute magnitude

import math

def abs_mag(M,D):
    m = M+5*math.log(D/10,10)         # m is apparent magnitude
    return m

def app_mag(m):
    F = (3.631*10**-20)*(10.**(m/-2.5))  # F0 = 3.631*10**-20
    return F

D = float(input("The effective radius in parsec: "))
M = float(input("The absolute magnitude is: "))
a = abs_mag(M,D)
b = app_mag(a)
print(a)
print(b)
