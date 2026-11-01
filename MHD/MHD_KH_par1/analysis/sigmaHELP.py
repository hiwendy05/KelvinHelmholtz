import pyPLUTO as pp
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

# =========================================================
# MACH NUMBER
# =========================================================

MachStr = ["0p5", "1p0", "1p5", "2p0", "2p5", "3p0"]

for M in MachStr:

    # =====================================================
    # Load .dat file
    # =====================================================

    D = pp.Load(
        path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/" + M
    )

    analysis = D.read_file("par1_kh" + M + ".dat")

    time = np.asarray(analysis["time"])
    vy2 = np.asarray(analysis["vy2"])

    # =====================================================
    # Find ALL local extrema
    # =====================================================

    localMax = argrelextrema(vy2, np.greater)[0]
    localMin = argrelextrema(vy2, np.less)[0]

    print("M =", M)
    print("Number of points =", len(time))
    print("Number of minima =", len(localMin))
    print("Number of maxima =", len(localMax))

    # =====================================================
    # Search for possible linear-growth intervals
    # =====================================================

    best_R2 = -np.inf
    best_start = None
    best_end = None
    best_fit = None

    # Ignore very early extrema, which are dominated by noise
    # Change this if necessary
    min_start_index = 20

    for minimum in localMin:

        if minimum < min_start_index:
            continue

        # Maxima after this minimum
        maxima_after = localMax[localMax > minimum]

        for maximum in maxima_after:

            # Need enough points in the interval
            if maximum - minimum < 30:
                continue

            x = time[minimum:maximum]
            y_data = vy2[minimum:maximum]

            # Must have positive values for log
            if np.any(y_data <= 0):
                continue

            y = np.log(y_data)

            # Linear fit
            fit = np.polyfit(x, y, 1)

            y_fit = np.polyval(fit, x)

            # Calculate R^2
            ss_res = np.sum((y - y_fit)**2)
            ss_tot = np.sum((y - np.mean(y))**2)

            if ss_tot == 0:
                continue

            R2 = 1.0 - ss_res / ss_tot

            # Keep the most linear interval
            if R2 > best_R2:

                best_R2 = R2
                best_start = minimum
                best_end = maximum
                best_fit = fit

    # =====================================================
    # Check result
    # =====================================================

    if best_start is None:

        print("Could not find a suitable linear-growth interval.")
        continue

    # =====================================================
    # Calculate growth rate
    # =====================================================

    x = time[best_start:best_end]
    y = np.log(vy2[best_start:best_end])

    slope = best_fit[0]

    # <vy^2> ~ exp(2 sigma t)
    sigma = slope / 2.0

    print()
    print("======================================")
    print("Selected linear-growth regime")
    print("======================================")
    print("Start index =", best_start)
    print("End index   =", best_end)
    print("Start time  =", time[best_start])
    print("End time    =", time[best_end])
    print("Number of points =", len(x))
    print("R^2 =", best_R2)
    print("Slope =", slope)
    print("Sigma =", sigma)
    print("======================================")
