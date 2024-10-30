import batman
import numpy as np
from matplotlib import pyplot as plt

params = batman.TransitParams()       #object to store transit parameters
params.t0 = 0.                        #time of inferior conjunction
params.per = 18.8805                       #orbital period
params.rp = .2436                      #planet radius (in units of stellar radii)
params.a = .1233                              #semi-major axis (in units of stellar radii)
params.inc = 89.61                      #orbital inclination (in degrees)
params.ecc = .093                       #eccentricity
params.w = 170.                        #longitude of periastron (in degrees)
params.limb_dark = "quadratic"        #limb darkening model
params.u = [0.59865, -0.159233]      #limb darkening coefficients [c1, c2]

t = np.linspace(-0.025, 0.025, 1000)  #times at which to calculate light curve
m = batman.TransitModel(params, t)    #initializes model

flux = m.light_curve(params)                    #calculates light curve

radii = np.linspace(0.23, 0.25, 20)
for r in radii:
        params.rp = r                           #updates planet radius
        new_flux = m.light_curve(params)        #recalculates light curve
