# Loading the relevant packages
import pyPLUTO as pp
import os
import numpy as np

# Load data
D = pp.Load()

# Creating the image and the subplot axes (to have two secondary plots)
Image = pp.Image(
    figsize=[10.5, 10],
    suptitle="HD Kelvin-Helmholtz instability test, M=0.5"
)
Image.create_axes(right=0.55)
Image.create_axes(nrow=2, hspace=[0.003], left=0.67)

# Plotting the data
Image.display(
    D.rho,
    x1=D.x1,
    x2=D.x2,
    title="Density",
    aspect="equal",
    ax=0,
    shading="gouraud",
    xtitle=r"$x$",
    ytitle=r"$y$",
    cpos="right",
)

# Find and plot the field lines
#lines = D.find_fieldlines(
#    D.Bx1,
#    D.Bx2,
#    x1=D.x1,
#    x2=D.x2,
#    y0=[0.0, 0.1, -0.1, 0.25, -0.25],
#    x0=[0.5, 0.5, 0.5, 0.5, 0.5],
#    order="RK45",
#    maxstep=0.001,
#    numsteps=10000,
#)

#for _, line in enumerate(lines):
#    Image.plot(line[0], line[1], ax=0, c="k")

# Find and plot vx2 field lines over density plot to show vortex sheet explicitly
Image.contour(
    D.vx2,
    levels=10,
    ax=Image.ax[0],
    x1=D.x1,
    x2=D.x2,
)

# Open the kh.dat file and store the variables
analysis = D.read_file("kh.dat")

# Calculate growth rate
sigma=np.gradient(np.log(analysis["vy2"]))*0.5
print(sigma)

# Add text in the axes
Image.text(r"$\langle v_y^2\rangle$", ax=1, x=0.05)
Image.text(r"$v_{y, MAX}$", ax=2, x=0.05)

# Plot the velocity from the kh.dat file.
Image.plot(
    analysis["time"],
    analysis["vy2"],
    ax=1,
    c="k",
    yscale="log",
    xtickslabels=None,
)
Image.plot(
    analysis["time"],
    analysis["maxvy"],
    ax=2,
    c="k",
    yscale="log",
    xtitle=r"$t$"
)

# Saving the image and showing the plots
output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/HD_KH_fin/plots"
Image.savefig(os.path.join(output_dir, "HD_KH_0p5.png"))
