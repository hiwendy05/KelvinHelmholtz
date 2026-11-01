import pyPLUTO as pp
import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt

# =========================================================
# Mach number
# =========================================================

M = "2p5"

# =========================================================
# Load PLUTO data
# =========================================================

D = pp.Load(
    path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/" + M,
    nout="all"
)

tot_out = 500

# =========================================================
# Calculate <vy^2> from the simulation data
# =========================================================

dV = (D.x1r[1] - D.x1r[0]) * (D.x2r[1] - D.x2r[0])

tot_vol = 2.0

vy2_av = []
Emagx_av = []
Emagy_av = []

for n in range(tot_out + 1):

    vy2 = 0.0
    Emagx = 0.0
    Emagy = 0.0

    for i in range(400):
        for j in range(800):

            vy2 += D.vx2[n][i][j]**2 * dV

            Emagx += D.Bx1[n][i][j]**2 * 0.5 * dV

            Emagy += D.Bx2[n][i][j]**2 * 0.5 * dV

    vy2_av.append(vy2 / tot_vol)
    Emagx_av.append(Emagx / tot_vol)
    Emagy_av.append(Emagy / tot_vol)

# Convert to numpy arrays
vy2_av = np.asarray(vy2_av)
Emagx_av = np.asarray(Emagx_av)
Emagy_av = np.asarray(Emagy_av)

# =========================================================
# Time array
# =========================================================

time = np.asarray(D.time[:tot_out + 1])

# =========================================================
# ORIGINAL METHOD
# Find local minimum and maximum
# =========================================================

localMax = argrelextrema(vy2_av, np.greater)
localMin = argrelextrema(vy2_av, np.less)

print("Local minima:")
print(localMin[0])

print()
print("Local maxima:")
print(localMax[0])

# =========================================================
# Select the minimum and maximum defining the
# linear-growth regime
#
# CHANGE THESE TWO NUMBERS once you identify the
# appropriate extrema.
# =========================================================

imin = 0
imax = 0

min_index = localMin[0][imin]
max_index = localMax[0][imax]

print()
print("Selected minimum index =", min_index)
print("Selected maximum index =", max_index)

print("Selected minimum time =", time[min_index])
print("Selected maximum time =", time[max_index])

# =========================================================
# Same calculation as your original code
# =========================================================

x = time[min_index:max_index]

y = np.log(
    vy2_av[min_index:max_index]
)

# =========================================================
# Line of best fit to log(<vy^2>)
# =========================================================

sigma = np.polyfit(x, y, 1)

# Divide by 2 because we fitted <vy^2>
growth_rate = sigma[0] * 0.5

print()
print(M + " Sigma =", growth_rate)
