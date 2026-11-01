Magnetic field in y direction only, i.e. perpendicular to shear layer

[Boundary]

X1-beg        periodic
X1-end        periodic
X2-beg        periodic
X2-end        periodic
X3-beg        outflow
X3-end        outflow

[Parameters]                   
                               
CSOUND                      1.0 
MACH                        0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0
SIGMA_POL                   0.01
SIGMA_TOR                   1.0

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
  v[BX1] = 0.0;
  v[BX2] = g_inputParam[SIGMA_POL];
  v[BX3] = g_inputParam[SIGMA_TOR];
