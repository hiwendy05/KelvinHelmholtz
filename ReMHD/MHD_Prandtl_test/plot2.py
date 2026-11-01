# Loading the relevant packages
import pyPLUTO as pp
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Load data
for i in range(11):
 output = 10*i
 D = pp.Load(path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_Prandtl/1p0", nout=output)

# Creating the image and the subplot axes (to have two secondary plots)
 Image = pp.Image(
    figsize=[20, 10],
    suptitle=r"Resistive MHD KHI, $P_m=1.0$"
 )
# Image.create_axes(right=0.5)
# Image.create_axes(nrow=2, hspace=[0.003], left=0.50)

# Plotting the data
 Image.display(
    D.rho,
    x1=D.x1,
    x2=D.x2,
    title=rf"Density, $t = ${D.timelist[output]:.1f}",
    aspect="equal",
    shading="gouraud",
    xtitle=r"$x$",
    ytitle=r"$y$",
    cpos="right",
 )

# Find and plot the field lines
 lines = D.find_fieldlines(
    D.Bx1,
    D.Bx2,
    x1=D.x1,
    x2=D.x2,
    y0=[0.0, 0.1, -0.1, 0.25, -0.25],
    x0=[0.5, 0.5, 0.5, 0.5, 0.5],
    order="RK45",
    maxstep=0.001,
    numsteps=10000,
 )

 for _, line in enumerate(lines):
    Image.plot(line[0], line[1], ax=0, c="k")
# Saving the image and showing the plots
 output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_Prandtl/plots"
 Image.savefig(os.path.join(output_dir, f"MHD_Prandtl_1p0_t={D.timelist[output]:.1f}.png"))
