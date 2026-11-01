# Loading the relevant packages
import pyPLUTO as pp
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Load data
for i in range(11):
 output = 50*i
 D = pp.Load(path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_Prandtl_test/1p0", nout=output)

# Creating the image and the subplot axes (to have two secondary plots)
 Image = pp.Image(
    figsize=[20, 10],
    suptitle=r"Resistive MHD KHI, $P_m=1.0$"
 )
 Image.create_axes(right=0.5)
 Image.create_axes(nrow=2, hspace=[0.003], left=0.50)

# Plotting the data
 Image.display(
    D.rho,
    x1=D.x1,
    x2=D.x2,
    title=rf"Density, $t = ${D.timelist[output]:.1f}",
    aspect="equal",
    ax=0,
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

# Open the kh.dat file and store the variables
 analysis = D.read_file("prandtl_1p0.dat")

# Calculate growth rate
#sigma=np.gradient(np.log(analysis["vy2"]))*0.5
#print(sigma)

# Add text in the axes
 Image.text(r"$\langle v_y^2\rangle$", ax=1, x=0.05)
 Image.text(r"$E_{mag}$", ax=2, x=0.05)

# Plot the velocity from the kh.dat file.
 Image.plot(
    analysis["time"],
    analysis["vy2"],
    ax=1,
    c="k",
    yscale="log",
    xtickslabels=None,
 )

 Image.ax[1].axvline(x=D.timelist[output], c="red")

# Calculate total energy of magnetic field
 Emag=analysis["Emagx"] + analysis["Emagy"] + analysis["Emagz"]

# Image.plot(
#    analysis["time"],
#    Emag,
#    ax=2,
#    xtitle=r"$t$",
#    yrange=[-0.01, 0.012]
# )
 Image.plot(
    analysis["time"],
    Emag,
    ax=2,
    xtitle=r"$t$",
    label=r"$E_{\text{mag}}$",
    legpos = 0
 )
 Image.plot(
    analysis["time"],
    analysis["Emagx"],
    ax=2,
    label=r"$E_{\text{mag, }x}$"
 )

# Image.plot(
#    analysis["time"],
#    analysis["Emagy"],
#    ax=2,
#    label=r"$E_{\text{mag, }y}$"
# )

# Image.plot(
#    analysis["time"],
#    analysis["Emagz"],
#    ax=2,
#    label=r"$E_{\text{mag, }z}$"
# )


 Image.ax[2].axvline(x=D.timelist[output], c="red")

# Saving the image and showing the plots
 output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_Prandtl_test/plots"
 Image.savefig(os.path.join(output_dir, f"MHD_Prandtl_1p0_t={D.timelist[output]:.1f}.png"))
