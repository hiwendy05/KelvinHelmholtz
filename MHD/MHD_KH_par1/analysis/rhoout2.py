import pyPLUTO as pp

D=pp.Load(path = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/1p5", nout=0)

dV= (1/400)*(2/800)
totrho = 0
for i in range(400):
 for j in range(800):
  totrho += D.rho[i][j] * dV
print(totrho)
