import pyPLUTO as pp
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Load data
D = pp.Load(path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par3/1p5")
analysis = D.read_file("par3_kh1p5.dat")

Image = pp.Image(suptitle="Total mass in domain over time, M=1.5")
Image.plot(analysis["time"], analysis["totrho"])

output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par3/plots"
Image.savefig(os.path.join(output_dir, f"MHD_KH_par3_1p5_rho.png"))
