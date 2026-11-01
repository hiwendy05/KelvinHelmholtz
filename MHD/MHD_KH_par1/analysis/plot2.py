# Loading the relevant packages
import pyPLUTO as pp
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Post calculation for <vy2>
data=pp.Load(path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/2p5", nout="all")
tot_out = 500 # Final output file number

dV = (data.x1r[1]-data.x1r[0]) * (data.x2r[1]-data.x2r[0]) # since uniform grid, dV is constant

vy2_av = []
Emagx_av = []
Emagy_av = []
Emag_av = []
tot_vol = 2

for n in range(tot_out+1):
  vy2 = 0
  Emagx = 0
  Emagy = 0
  for i in range(400):
    for j in range(800):
      vy2 += (data.vx2[n][i][j]**2) *dV
      Emagx += (data.Bx1[n][i][j]**2) * 0.5 * dV
      Emagy += (data.Bx2[n][i][j]**2) * 0.5 * dV

  vy2_av.append(vy2/tot_vol)
  Emagx_av.append(Emagx/tot_vol)
  Emagy_av.append(Emagy/tot_vol)
  Emag_av.append((Emagx+Emagy)/tot_vol)

# Load data
for i in range(11):
 output = 50*i
 D = pp.Load(path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/2p5", nout=output)

# Creating the image and the subplot axes (to have two secondary plots)
 Image = pp.Image(
    figsize=[20, 10],
    suptitle="MHD KHI, parallel magnetic field, M=2.5"
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
# analysis = D.read_file("par1_kh0p1.dat")

# Calculate growth rate
#sigma=np.gradient(np.log(analysis["vy2"]))*0.5
#print(sigma)

# Add text in the axes
 Image.text(r"$\langle v_y^2\rangle$", ax=1, x=0.05)
 Image.text(r"$E_{mag}$", ax=2, x=0.05)

# Plot <vy2> against time from post-processing
 Image.plot(x=D.timelist, y=vy2_av, ax=1, c="k", yscale="log", xtickslabels=None)
 Image.ax[1].axvline(x=D.timelist[output], c="red")

# Calculate total energy of magnetic field
 Image.plot(x=D.timelist, y=Emag_av, ax=2, xtitle=r"$t$", label=r"$E_{\text{mag}}$", legpos=0)

 Image.plot(
    x=D.timelist,
    y=Emagx_av,
    ax=2,
    label=r"$E_{\text{mag, }x}$"
 )

 Image.plot(
    x=D.timelist,
    y=Emagy_av,
    ax=2,
    label=r"$E_{\text{mag, }y}$"
 )

# Image.plot(
#    analysis["time"],
#    analysis["Emagz"],
#    ax=2,
#    label=r"$E_{\text{mag, }z}$"
# )


 Image.ax[2].axvline(x=D.timelist[output], c="red")

# Saving the image and showing the plots
 output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/plots"
 Image.savefig(os.path.join(output_dir, f"MHD_KH_par1_2p5_t={D.timelist[output]:.1f}.png"))
