from astropy.cosmology import FlatLambdaCDM
import numpy as np
from astropy import units as u
cosmo = FlatLambdaCDM(H0=72, Om0=0.26)

d_A = cosmo.angular_diameter_distance(z=1.0) 

theta = 0.439 ### *u.arcsec <-- not needed  #theta in arcsec = 0.439
distance_pc = (theta * d_A).to(u.pc, u.dimensionless_angles()) 

print(distance_pc)
