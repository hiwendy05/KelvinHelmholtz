BNS merger event happens in the speed of approximately 0.1c sos we modify our VEL0 for a more suitable simulation for BNS mergers.

[Boundary]

X1-beg        periodic
X1-end        periodic
X2-beg        outflow
X2-end        outflow
X3-beg        outflow
X3-end        outflow

[Parameters]                   
                               
VEL0                        0.1
MACH                        0.5, 1.0
SIGMA_POL                   0.01
SIGMA_TOR                   0.0

[Initial setup]

  arg = g_inputParam[MACH]/g_inputParam[VEL0];
  arg = arg*arg;
  #if EOS == IDEAL
    g_gamma = 4./3.;
    pr0 = (g_gamma - 1.0)/((g_gamma - 1.0)*arg - 1.0)/g_gamma;
  
  kx    = 2.0*CONST_PI*x1;
  alpha = 0.01;
  beta  = 0.1;

  arg = y*y/(beta*beta);
  eps = 0.5e-4*g_inputParam[MACH];

  v[RHO] = 1.0;
  v[VX1] = -g_inputParam[VEL0]*tanh(y/alpha); /*finite width*/
  v[VX2] =  eps*0.5*(sin(kx) - sin(-kx))*exp(-arg); /* perturbation */
  v[VX3] = 0.0;

  v[BX1] = sqrt(2.0*g_inputParam[SIGMA_POL]);
  v[BX2] = 0.0;
  v[BX3] = sqrt(2.0*g_inputParam[SIGMA_TOR]);

