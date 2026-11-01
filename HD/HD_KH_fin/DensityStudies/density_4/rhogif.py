import pyPLUTO as pp
import os

D = pp.Load(
    var="rho",
    nout="all"
)

I=pp.Image(suptitle="HD KHI Density, M=1.5")
I.interactive(D.rho, x1=D.x1, x2=D.x2, cpos="right")
output_dir="/cephfs/store/astro-hl278/hc636/PLUTO_DATA/HD_KH_fin/plots"
I.animate(os.path.join(output_dir, "density.gif" ))
