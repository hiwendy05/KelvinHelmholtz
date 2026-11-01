#define  PHYSICS                        RMHD
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

#define  EOS                            IDEAL
#define  ENTROPY_SWITCH                 NO
#define  RADIATION                      NO
#define  DIVB_CONTROL                   CONSTRAINED_TRANSPORT

/* -- user-defined parameters (labels) -- */

#define  VEL0                           0
#define  MACH                           1
#define  SIGMA_POL                      2
#define  SIGMA_TOR                      3

/* [Beg] user-defined constants (do not change this line) */


/* [End] user-defined constants (do not change this line) */
