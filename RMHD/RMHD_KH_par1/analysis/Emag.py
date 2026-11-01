import pyPLUTO as pp
import os
import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt

D=pp.Load(path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/RMHD_KH_par1/0p5", nout="all")
tot_out = 500 # Final output file number
#analysis = D.read_file("par1_kh0p1.dat")

# Post calculation for <vy2>
dV = (D.x1r[1]-D.x1r[0]) * (D.x2r[1]-D.x2r[0]) # since uniform grid, dV is constant
#vy2_av = []
Emagx_av = []
Emagy_av = []
tot_vol = 2

for n in range(tot_out+1):
 # vy2 = 0
  Emagx = 0
  Emagy = 0
#  tot_vol = 0
  for i in range(400):
    for j in range(800):
 #     vy2 += (D.vx2[n][i][j]**2) *dV
      Emagx += (D.Bx1[n][i][j]**2) * 0.5 * dV
      Emagy += (D.Bx2[n][i][j]**2) * 0.5 * dV
#      tot_vol += dV
#  vy2_av.append(vy2/tot_vol)
  Emagx_av.append(Emagx/tot_vol)
  Emagy_av.append(Emagy/tot_vol)

Emag=Emagx_av + Emagy_av
Emag0 = Emag[0]
EmagMax = np.max(Emag)
amp = EmagMax/Emag0
print("0p5", str(amp))

MachStr = ["1p0", "1p5", "2p0", "2p5", "3p0"]
#MachStr = ["3p0"]
amp = []
for i in range(len(MachStr)):
 M = MachStr[i]
 D=pp.Load(path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/RMHD_KH_par1/"+M)

 analysis = D.read_file("par1_kh"+M+".dat")

# Find the local minimum and maximum to identify the linear regime
 Emag=analysis["Emagx"] + analysis["Emagy"] + analysis["Emagz"]
 Emag0 = Emag[0]
 EmagMax = np.max(Emag)
 amp.append(EmagMax/Emag0)

 print(M, str(amp[i]))
#sigma=np.polyfit(x, y, 1) #line of best fit for t-log<vy2>

#figure = plt.figure(title="Magnetic energy amplification for different Mach numbers")
#x = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
#figure.plot(x, amp)
#output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/plots"
#figure.savefig(os.path.join(output_dir, f"MHD_par1_amp.png"))
#print(M+" Sigma = "+str(sigma[0]*0.5)) # halve because we found for vy^2
figure = plt.figure()
plt.title("Magnetic energy amplification for different Mach numbers")

x = [1.0, 1.5, 2.0, 2.5, 3.0]
plt.plot(x, amp)

output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/RMHD_KH_par1/plots"
figure.savefig(os.path.join(output_dir, "RMHD_par1_amp.png"))
