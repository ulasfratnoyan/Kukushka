import batman
import numpy as np
from matplotlib import pyplot as plt

params = batman.TransitParams()       #object to store transit parameters
params.t0 = 0.                        #time of inferior conjunction
params.per = 18.8805                       #orbital period
params.rp = .03523                     #planet radius (in units of stellar radii)
params.a = 37.31                              #semi-major axis (in units of stellar radii)
params.inc = 89.61                      #orbital inclination (in degrees)
params.ecc = .093                       #eccentricity
params.w = 170.                        #longitude of periastron (in degrees)
params.limb_dark = "quadratic"        #limb darkening model
params.u = [0.59865, -0.159233]      #limb darkening coefficients [c1, c2]

t = np.linspace(-0.3, 0.3, 1000)  #times at which to calculate light curve
m = batman.TransitModel(params, t)    #initializes model

flux = m.light_curve(params)                    #calculates light curve

plt.figure()

m = batman.TransitModel(params, t)        #initializes the model
flux = m.light_curve(params)              #calculates light curve
plt.plot(t, flux, label = params.limb_dark)
plt.savefig("HD73583Ac_asssignment1_taskF.png")
