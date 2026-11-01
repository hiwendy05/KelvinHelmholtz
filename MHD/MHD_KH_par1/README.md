# MHD_KH_par1
Back to purely x magnetic field, but with weaker strength. Issue with out1 is likely to be that magnetic field was too strong, suppressing the instability.

[Boundary]

X1-beg        periodic
X1-end        periodic
X2-beg        outflow
X2-end        outflow
X3-beg        outflow
X3-end        outflow

[Parameters]

CSOUND                      1.0
MACH                        0.1, 0.5, 1.0, 1.5, 2.0,2.5, 3.0
SIGMA_POL                   0.01
SIGMA_TOR                   0.0

[Initial setup]
  kx    = 2.0*CONST_PI*x1;
  alpha = 0.01;
  beta  = 0.1;

  arg = y*y/(beta*beta);
  eps = 0.5e-4*g_inputParam[MACH];

  v[RHO] = 1.0; /* uniform density */
  v[VX1] = -g_inputParam[MACH]*0.5*tanh(y/alpha); /*finite width*/
  v[VX2] =  eps*0.5*(sin(kx) - sin(-kx))*exp(-arg); /* perturbation */
  v[VX3] = 0.0;

  v[BX1] = sqrt(2.0*g_inputParam[SIGMA_POL]);
  v[BX2] = 0.0;
  v[BX3] = sqrt(2.0*g_inputParam[SIGMA_TOR]);

