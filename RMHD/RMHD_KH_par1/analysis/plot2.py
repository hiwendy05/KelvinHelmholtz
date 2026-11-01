# Loading the relevant packages
import pyPLUTO as pp
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Post calculation for <vy2>
data=pp.Load(path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/0p5", nout="all")
tot_out = 500 # Final output file number

dV = (data.x1r[1]-data.x1r[0]) * (data.x2r[1]-data.x2r[0]) # since uniform grid, dV is constant

vy2_av = []
time =[]
#Emagx_av = []
#Emagy_av = []
#Emag_av = []
tot_vol = 2

for n in range(tot_out+1):
  vy2 = 0
#  Emagx = 0
#  Emagy = 0
  for i in range(400):
    for j in range(800):
      vy2 += (data.vx2[n][i][j]**2) *dV
#      Emagx += (data.Bx1[n][i][j]**2) * 0.5 * dV
#      Emagy += (data.Bx2[n][i][j]**2) * 0.5 * dV

  vy2_av.append(vy2/tot_vol)
  time.append(data.timelist[n])

#  Emagx_av.append(Emagx/tot_vol)
#  Emagy_av.append(Emagy/tot_vol)
#  Emag_av.append((Emagx+Emagy)/tot_vol)

# Load data
#for i in range(11):
# output = 50*i
# D = pp.Load(path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/2p5", nout=output)

figure = plt.figure()
figure.plot(x=time, y=vy2_av)
figure.title("<vy2> for M=0.5")

output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/RMHD_KH_par1/plots"
figure.savefig(os.path.join(output_dir, "RMHD_par1_0p5_vy2.png"))
