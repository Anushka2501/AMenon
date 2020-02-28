##Flux from absolute magnitude

import math

def absmag_to_appmag(M,D):
    app_mag = M+5*math.log(D/10,10)         # m is apparent magnitude
    return app_mag

def appmag_to_flux(app_mag):
    flux = 10**((25-app_mag)/2.5)        # zp mag = 24  
    return flux

D = float(input("The effective radius in parsec: "))
M = float(input("The absolute magnitude is: "))
a = absmag_to_appmag(M,D)
b = appmag_to_flux(a)
print(a)
print(b)
