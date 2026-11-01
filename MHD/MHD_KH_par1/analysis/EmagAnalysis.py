import pyPLUTO as pp
import numpy as np
import os
D=pp.Load(path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/2p5", nout="all")
tot_out = 500 # Final output file number
#analysis = D.read_file("par1_kh0p1.dat")

# Post calculation for <vy2>
dV = (D.x1r[1]-D.x1r[0]) * (D.x2r[1]-D.x2r[0]) # since uniform grid, dV is constant
vy2_av = []
Emagx_av = []
Emagy_av = []
tot_vol = 2

for n in range(tot_out+1):
  vy2 = 0
  Emagx = 0
  Emagy = 0
#  tot_vol = 0
  for i in range(400):
    for j in range(800):
      vy2 += (D.vx2[n][i][j]**2) *dV
      Emagx += (D.Bx1[n][i][j]**2) * 0.5 * dV
      Emagy += (D.Bx2[n][i][j]**2) * 0.5 * dV
#      tot_vol += dV
  vy2_av.append(vy2/tot_vol)
  Emagx_av.append(Emagx/tot_vol)
  Emagy_av.append(Emagy/tot_vol)

#print(vy2_av)

# Plot <vy2> against time
Image=pp.Image()
Image.plot(x=D.timelist, y=vy2_av, title=r"$\langle v_y^2 \rangle$ for MHD KHI, M=0.1")


# Saving the image and showing the plots
output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/plots"
Image.savefig(os.path.join(output_dir, "MHD_KH_par1_vy2_0p1.png"))
