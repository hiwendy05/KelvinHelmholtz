import pyPLUTO as pp
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Load data
D = pp.Load(path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/1p5")
analysis = D.read_file("par1_kh1p5.dat")

Image = pp.Image(suptitle="Total density in domain over time, M=1.5")
Image.plot(analysis["time"], analysis["totrho"], xtitle="t", ytitle=r"$\rho$")

output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/plots"
Image.savefig(os.path.join(output_dir, "MHD_KH_par1_1p5_rho.png"))
