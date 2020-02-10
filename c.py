##Velocity Dispersion

def luminosity(h,R):       
    L = ((10**10.2*h**-2)*(R/10**0.52*h**-1)**1.5)
    return L

def vel_dispersion(L,h):
    sigma = (((L/10**10.2*h**-2)**0.25)*10**2.197)
    return sigma

R = float(input("Enter the effective radius in kpc: "))
h = float(0.72/0.7)           # h=h70 is reduced Hubbles constant
L = luminosity(h,R)           # In terms of solar luminosity
sigma = vel_dispersion(L,h)
print(L)
print(sigma)


