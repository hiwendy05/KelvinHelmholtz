#define  PHYSICS                        MHD
#define  DIMENSIONS                     2
#define  GEOMETRY                       CARTESIAN
#define  BODY_FORCE                     NO
#define  COOLING                        NO
#define  RECONSTRUCTION                 LINEAR
#define  TIME_STEPPING                  HANCOCK
#define  NTRACER                        0
#define  PARTICLES                      NO
#define  USER_DEF_PARAMETERS            4

/* -- physics dependent declarations -- */

#define  EOS                            ISOTHERMAL
#define  ENTROPY_SWITCH                 NO
#define  DIVB_CONTROL                   CONSTRAINED_TRANSPORT
#define  BACKGROUND_FIELD               NO
#define  AMBIPOLAR_DIFFUSION            NO
#define  RESISTIVITY                    NO
#define  HALL_MHD                       NO
#define  THERMAL_CONDUCTION             NO
#define  VISCOSITY                      NO
#define  RADIATION                      NO
#define  ROTATING_FRAME                 NO
#define  CT_EMF_AVERAGE			UCT_CONTACT

/* -- user-defined parameters (labels) -- */

#define  CSOUND                         0
#define  MACH                           1
#define  SIGMA_POL                      2
#define  SIGMA_TOR                      3

/* [Beg] user-defined constants (do not change this line) */


/* [End] user-defined constants (do not change this line) */
