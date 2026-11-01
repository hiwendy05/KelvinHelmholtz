import pyPLUTO as pp
import numpy as np
from scipy.signal import argrelextrema

#MachStr = ["0p5", "1p0", "1p5", "2p0", "2p5", "3p0"]
MachStr = ["3p0"]
for i in range(len(MachStr)):
 M = MachStr[i]
 D=pp.Load(path="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par3/"+M)

#sigma=np.gradient(np.log(analysis["vy2"][0:))*0.5
 analysis = D.read_file("par3_kh"+M+".dat")

# Find the local minimum and maximum to identify the linear regime
 localMax=argrelextrema(np.log(analysis["vy2"]), np.greater)
 localMin=argrelextrema(np.log(analysis["vy2"]), np.less)
 print(localMin[0][1], localMax[0][1])
 print(localMax[0])
#np.gradient(np.log(analysis["vy2"][localMin[0][0]:localMax[0][0]]))*0.5

 x = analysis["time"][localMin[0][1]:localMax[0][1]]
 y = np.log(analysis["vy2"][localMin[0][1]:localMax[0][1]])
 sigma=np.polyfit(x, y, 1) #line of best fit for t-log<vy2>
 print(M+" Sigma = "+str(sigma[0]*0.5)) # halve because we found for vy^2
