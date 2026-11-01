# Loading the relevant packages
import pyPLUTO as pp
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Load data
for i in range(50):
 output =10*i
 D = pp.Load(path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/RMHD_KH_par1/0p5", nout=output)

# Creating the image and the subplot axes (to have two secondary plots)
 Image = pp.Image(
    figsize=[20, 10],
    suptitle="RMHD KHI, parallel magnetic field, M=0.5"
 )
 Image.create_axes(right=0.5)
 Image.create_axes(nrow=2, hspace=[0.003], left=0.50)

# Plotting the data
 Image.display(
    D.rho,
    x1=D.x1,
    x2=D.x2,
    title=rf"$\rho/\rho_0,\quad t = {D.timelist[output]:.1f}\,L_0 c^{{-1}}$",
    aspect="equal",
    ax=0,
    shading="gouraud",
    xtitle=r"$x$",
    ytitle=r"$y$",
    cpos="right"
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
 analysis = D.read_file("par1_kh0p5.dat")

# Calculate growth rate
#sigma=np.gradient(np.log(analysis["vy2"]))*0.5
#print(sigma)

# Add text in the axes
# Image.text(r"$\langle v_y^2\rangle / {c_s}^2$", ax=1, x=0.05)
# Image.text(r"$E_{mag} / \sigma_{\text{pol}0}$", ax=2, x=0.05)

# Plot the velocity from the kh.dat file.
 Image.plot(
    analysis["time"],
    analysis["vy2"],
    ax=1,
    c="k",
    yscale="log",
    xtickslabels=None,
    label=r"$\langle v_y^2\rangle / {c}^2$",
    legpos = 0
 )

 Image.ax[1].axvline(x=D.timelist[output], c="red")

# Calculate total energy of magnetic field
 Emag=analysis["Emagx"] + analysis["Emagy"] + analysis["Emagz"]

# Image.plot(
#    analysis["time"],
#    Emag,
#    ax=2,
#    xtitle=r"$t$",
#    ytitle=r"Magnetic energy $/\sigma_{\text{pol}0}$"
# )
 Image.plot(
    analysis["time"],
    Emag,
    ax=2,
    xtitle=r"Time $/L_0 c^{-1}$",
    label=r"$E_{\text{mag}}/\sigma_{\text{pol}0}$",
    legpos = 0
 )

 Image.plot(
    analysis["time"],
    analysis["Emagx"],
    ax=2,
    label=r"$E_{\text{mag, }x}/\sigma_{\text{pol}0}$"
 )

 Image.plot(
    analysis["time"],
    analysis["Emagy"],
    ax=2,
    label=r"$E_{\text{mag, }y}/\sigma_{\text{pol}0}$"
 )

# Image.plot(
#    analysis["time"],
#    analysis["Emagz"],
#    ax=2,
#    label=r"$E_{\text{mag, }z}$"
# )


 Image.ax[2].axvline(x=D.timelist[output], c="red")

# Saving the image and showing the plots
 output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/RMHD_KH_par1/plots"
 Image.savefig(os.path.join(output_dir, f"RMHD_KH_slides_t={D.timelist[output]:.1f}.png"))
