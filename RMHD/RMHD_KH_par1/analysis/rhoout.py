import pyPLUTO as pp
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Load data
D = pp.Load(path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/RMHD_KH_par1/0p5")
analysis = D.read_file("par1_kh0p5.dat")

Image = pp.Image(suptitle="Total mass in domain over time, M=1.5")
Image.plot(analysis["time"], analysis["mass"], xtitle="t", ytitle=r"m")

output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/RMHD_KH_par1/plots"
Image.savefig(os.path.join(output_dir, "RMHD_KH_par1_0p5_mass.png"))
