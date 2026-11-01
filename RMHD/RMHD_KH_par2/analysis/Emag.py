import pyPLUTO as pp
import os
import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt

MachStr = ["0p5", "1p0", "1p5", "2p0", "2p5", "3p0"]
#MachStr = ["3p0"]
amp = []
for i in range(len(MachStr)):
 M = MachStr[i]
# pathName = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/"+
 D=pp.Load(path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/"+M)

#sigma=np.gradient(np.log(analysis["vy2"][0:))*0.5
 analysis = D.read_file("par1_kh"+M+".dat")

# Find the local minimum and maximum to identify the linear regime
 #localMax=argrelextrema(analysis["vy2"], np.greater)
 #localMin=argrelextrema(analysis["vy2"], np.less)
 Emag=analysis["Emagx"] + analysis["Emagy"] + analysis["Emagz"]
 Emag0 = Emag[0]
 EmagMax = np.max(Emag)
 amp.append(EmagMax/Emag0)
#np.gradient(np.log(analysis["vy2"][localMin[0][0]:localMax[0][0]]))*0.5

#x = analysis["time"][localMin[0][0]:localMax[0][0]]
#y = np.log(analysis["vy2"][localMin[0][0]:localMax[0][0]])
#sigma=np.polyfit(x, y, 1) #line of best fit for t-log<vy2>

#figure = plt.figure(title="Magnetic energy amplification for different Mach numbers")
#x = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
#figure.plot(x, amp)
#output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/plots"
#figure.savefig(os.path.join(output_dir, f"MHD_par1_amp.png"))
#print(M+" Sigma = "+str(sigma[0]*0.5)) # halve because we found for vy^2
figure = plt.figure()
plt.title("Magnetic energy amplification for different Mach numbers")

x = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
plt.plot(x, amp)

output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/plots"
figure.savefig(os.path.join(output_dir, "MHD_par1_amp.png"))
