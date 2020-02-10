##PSF for FWHM=0.8arcsec

from astropy.modeling import models
import numpy as np
import matplotlib.pyplot as plt

y,x = np.mgrid[-5:5,-5:5]
g = models.Gaussian2D(amplitude=0.1, x_mean=0, y_mean=0, x_stddev=1.698643633, y_stddev=1.698643633, theta=None)   # Tried by varying amplitudes but didn't observe any change
plt.imshow(g(y,x))
plt.show()
plt.savefig(psf.png)
