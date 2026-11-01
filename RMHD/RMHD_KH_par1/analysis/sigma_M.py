import matplotlib.pyplot as plt
import os

# sigma_pol = 0.01 (two points)

RM_001 = [0.5, 1.0]
Rsigma_001 = [
    1.4810568555905825,
    0.4522862547428144
]

# sigma_pol = 0.05 (one point, par2)
RM_005 = [0.5]
Rsigma_005 = [1.1461140036397703]

# Plot RMHD
plt.figure(figsize=(10,6))

plt.plot(
    RM_001, Rsigma_001,
    marker='o', linestyle=':',
    color='salmon', linewidth=2, markersize=10,
    label=r'RMHD, $\sigma_{\mathrm{pol}} = 0.01$'
)

plt.plot(
    RM_005, Rsigma_005,
    marker='s', linestyle='None',
    color='y', markersize=10,
    label=r'RMHD, $\sigma_{\mathrm{pol}} = 0.05$'
)

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

# Plot MHD
plt.plot(
    M_001, sigma_001,
    marker='o', linestyle='-',
    linewidth=2, markersize=10,
    color='royalblue',
    label=r'MHD, $\sigma_{\mathrm{pol}} = 0.01$'
)

plt.plot(
    M_005, sigma_005,
    marker='s', linestyle='-',
    linewidth=2, markersize=10,
    color='darkorange',
    label=r'MHD, $\sigma_{\mathrm{pol}} = 0.05$'
)

plt.plot(
    M_01, sigma_01,
    marker='^', linestyle='-',
    linewidth=2, markersize=10,
    color='forestgreen',
    label=r'MHD, $\sigma_{\mathrm{pol}} = 0.1$'
)


# Labels and title
plt.xlabel(r'Mach number, $M$', fontsize=30, labelpad=15)
plt.ylabel(r'Growth rate, $\sigma/L_0^{-1} c_s$', fontsize=30, labelpad=15)
plt.title(
    'MHD vs RMHD: Growth Rates for Different M',
    fontsize=30, pad=17
)

# Formatting
plt.legend(fontsize=15, loc=1)
plt.grid(True, linestyle=':', alpha=0.7)
plt.xlim(0.3, 3.2)
plt.ylim(bottom=0)
plt.xticks([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
plt.tick_params(axis='both', labelsize=15)

plt.tight_layout()

output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/RMHD_KH_par1/plots"
plt.savefig(os.path.join(output_dir, 'RMHD_sigma_vs_M.png'), dpi=300, bbox_inches='tight')
