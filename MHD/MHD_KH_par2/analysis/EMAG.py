import pyPLUTO as pp
import os
import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt

MachStr = ["0p5", "1p0", "1p5", "2p0", "2p5", "3p0"]
amps = []
for M in MachStr:

    # =====================================================
    # Load .dat file
    # =====================================================

    D = pp.Load(
        path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par2/" + M
    )

    analysis = D.read_file("par3_kh" + M + ".dat")
    Emag=analysis["Emagx"] + analysis["Emagy"] + analysis["Emagz"]
    Emag0 = Emag[0]
    EmagMax = np.max(Emag)
    amp = EmagMax/Emag0
    amps.append(amp)
print(amps)

