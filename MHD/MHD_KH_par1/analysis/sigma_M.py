import numpy as np
import matplotlib.pyplot as plt
import os

# Data for sigma_pol = 0.01
M_001 = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
sigma_001 = [
    1.4304297072260033,
    3.5948967540045285,
    3.636697879701209,
    2.5113018142150305,
    1.1456888977440696,
    1.0687468967051852
]

# Data for sigma_pol = 0.05
M_005 = [1.0, 1.5, 2.0, 2.5]
sigma_005 = [
    2.1652280521179326,
    3.02992999820263,
    2.1920087565093507,
    1.0284232341999815
]

# Data for sigma_pol = 0.1
M_01 = [1.0, 1.5, 2.0, 2.5]
sigma_01 = [
    0.8528046998031655,
    2.567707031678618,
    2.052372904282863,
    1.2728076871602483
]

# Plot
plt.figure(figsize=(10, 6))

plt.plot(
    M_001, sigma_001,
    marker='o', linestyle='-',
    linewidth=2, markersize=6,
    label=r'$\sigma_{\mathrm{pol}} = 0.01$'
)

plt.plot(
    M_005, sigma_005,
    marker='s', linestyle='--',
    linewidth=2, markersize=6,
    label=r'$\sigma_{\mathrm{pol}} = 0.05$'
)

plt.plot(
    M_01, sigma_01,
    marker='^', linestyle='-.',
    linewidth=2, markersize=6,
    label=r'$\sigma_{\mathrm{pol}} = 0.1$'
)

# Axis labels
plt.xlabel(r'Mach number, $M$', fontsize=30, labelpad=15)
plt.ylabel(r'Growth rate, $\sigma/L_0^{-1} c_s$', fontsize=30, labelpad=15)

# Formatting
plt.legend(fontsize=22, loc=1)
plt.grid(True, linestyle=':', alpha=0.7)
plt.tick_params(axis='both', labelsize=15)
plt.xlim(0.3, 3.2)
plt.ylim(bottom=0)

plt.title('MHD KHI: Growth Rates for Different Mach Numbers', fontsize=30, pad=17)

plt.tight_layout()
# Saving the image and showing the plots
output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/plots"
plt.savefig(os.path.join(output_dir, 'MHD_par1_sigma_vs_M.png'), dpi=300, bbox_inches='tight')
