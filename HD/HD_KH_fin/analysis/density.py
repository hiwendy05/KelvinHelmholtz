import pyPLUTO as pp
import os

D=pp.Load(var="rho")
nplots=len(D.rho)
I=pp.Image(suptitle="HD KHI Density plots, M=1.5")
I.create_axes(ncol=nplots)

for i in range(nplots):
    I.display(D.rho[i], x1=D.x1r, x2=D.x2r, cpos="right", ax=i, title=rf"$\rho$, $t = ${D.timelist[i]:.1f}")

output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/HD_KH_fin/plots"
I.savefig(os.path.join(output_dir, "density.pdf" ))
