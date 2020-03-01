import sncosmo
import matplotlib.pyplot as plt
import numpy as np

model = sncosmo.Model('hsiao')
model.set(z=1.0, t0=1.)
model.set_source_peakabsmag(-19,'besselli','ab')
timeax=np.linspace(-10,100,200)
abg=model.bandflux(['sdssg'], timeax, zp=25, zpsys='ab')
abr=model.bandflux(['sdssr'], timeax, zp=25, zpsys='ab')
abi=model.bandflux(['sdssi'], timeax, zp=25, zpsys='ab')

ax=plt.subplot(2,2,1)
ax.plot(timeax,abg)
ax.plot(timeax,abr)
ax.plot(timeax,abi)
plt.xlabel('Time in days')
plt.ylabel('Flux in counts')
plt.show()
