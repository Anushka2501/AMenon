##PSF 1pixel = 0.2arcsec
##FWHM = 0.8arcsec = 4pixel
##sigma_x = sigma_y = 1.698643633

import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models

y,x = np.mgrid[-5:5, -5:5]
g = models.Gaussian2D(amplitude=1.0, x_mean=0, y_mean=0, x_stddev=1.698643633, y_stddev=1.698643633, theta=None)
plt.figure(figsize=(2.5,2.5))
plt.imshow(g(x,y), origin='lower')
plt.show()
