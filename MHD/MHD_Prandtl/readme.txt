Followed setup in Loren E. Held's paper. Eta fixed at 0.000005 with different Prandtl numbers Pm = 1, 2, 4, 8.

[Boundary]

X1-beg        periodic
X1-end        periodic
X2-beg        outflow
X2-end        outflow
X3-beg        outflow
X3-end        outflow

[Parameters]                   
                               
CSOUND                      1.0
MACH                        1.5
SIGMA_POL                   0.01
SIGMA_TOR                   0.0
NU_VISC                     0.000005
ETA                         0.000005


[Initial setup]
  kx    = 2.0*CONST_PI*x1; /* wavenumber */
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

