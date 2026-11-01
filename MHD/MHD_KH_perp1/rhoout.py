import pyPLUTO as pp
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Load data
D = pp.Load(path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_perp1/0p5")
analysis = D.read_file("perp1_kh0p5.dat")

Image = pp.Image(suptitle="Total mass in domain over time, M=0.5")
Image.plot(analysis["time"], analysis["totrho"], xtitle="t", ytitle=r"$\rho$")

output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_perp1/plots"
Image.savefig(os.path.join(output_dir, "MHD_KH_perp1_0p5_rho.png"))
