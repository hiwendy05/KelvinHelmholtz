import pyPLUTO as pp
import os
Mlist = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
Mpath = ["0p5", "1p0", "1p5", "2p0", "2p5", "3p0"]
for j in range(6):
 
 for i in range(1):
  mach = Mlist[j]
  output=195
  load_path = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/RMHD_KH_par1/"+Mpath[j]
#  D=pp.Load(path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/RMHD_KH_par1/0p5", nout=output)
  D=pp.Load(path=load_path, nout=output) 

  Image = pp.Image(
    figsize=[20, 10],
    suptitle="RMHD KHI, parallel magnetic field, M="+str(mach)
  )

  Image.create_axes(right=0.5)
  Image.create_axes(nrow=2, hspace=[0.003], left=0.50)

# Plotting the data
  Image.display(
    D.Bx1,
    x1=D.x1,
    x2=D.x2,
    title=rf"$B_x$, $t = ${D.timelist[output]:.1f}",
    aspect="equal",
    ax=0,
    shading="gouraud",
    xtitle=r"$x$",
    ytitle=r"$y$",
    cpos="right",
  )

# Open the kh.dat file and store the variables
  ana_path = "par1_kh"+Mpath[j]+".dat"
  analysis = D.read_file(ana_path)

# Add text in the axes
  Image.text(r"$\langle v_y^2\rangle$", ax=1, x=0.05)
  Image.text(r"$E_{mag, x}$", ax=2, x=0.05)

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
# Emag=analysis["Emagx"] + analysis["Emagy"] + analysis["Emagz"]

# Image.plot(
#    analysis["time"],
#    Emag,
#    ax=2,
#    xtitle=r"$t$"
# )

  Image.plot(
    analysis["time"],
    analysis["Emagx"],
    ax=2,
    label=r"$E_{\text{mag, }x}$"
  )
  Image.ax[2].axvline(x=D.timelist[output], c="red")

# Saving the image and showing the plots
  output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/RMHD_KH_par1/plots"
  Image.savefig(os.path.join(output_dir, f"Prs_par1_"+Mpath[j]+"_t={D.timelist[output]:.1f}.png"))
