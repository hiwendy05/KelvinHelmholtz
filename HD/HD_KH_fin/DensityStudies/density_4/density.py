import pyPLUTO as pp
import os

D = pp.Load(
    var="rho",
    nout="all"
)
#D=pp.Load(var="rho")
nplots=8
I=pp.Image(suptitle="HD KHI Density plots, M=1.5")
I.create_axes(nrow=2, ncol=4)

for i in range(nplots):
    I.display(D.rho[i+2], x1=D.x1r, x2=D.x2r, cpos="right", ax=i, title=rf"$\rho$, $t = ${D.timelist[i+2]:.1f}")
    print(i+2)

output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/HD_KH_fin/plots"
I.savefig(os.path.join(output_dir, "density_t=10p0.pdf" ))
