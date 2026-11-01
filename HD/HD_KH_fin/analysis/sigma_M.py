import matplotlib.pyplot as plt
import os

# Data
M = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]

sigma = [
    0.013419807586955379,
    0.09953848544316794,
    0.12904472468273026,
    0.1346937095607748,
    0.08805003128693698,
    0.07850621813379222,
    0.0690388173069667,
    0.05146835429501805
]

# Plot
plt.figure(figsize=(10, 6))

plt.plot(
    M, sigma,
    marker='o',
    linestyle='-',
    color='royalblue',
    linewidth=2,
    markersize=6,
    label='HD'
)

# Labels and title
plt.xlabel(r'Mach number, $M$', fontsize=30, labelpad=10)
plt.ylabel(r'Growth rate, $\sigma/L_0^{-1} c_s$', fontsize=30, labelpad=10)
plt.title(
    'HD: Growth Rates for Different Mach Numbers',
    fontsize=30,
    pad=17
)

# Formatting
plt.legend(fontsize=20)
plt.grid(True, linestyle=':', alpha=0.7)
plt.tick_params(axis='both', labelsize=15)
plt.xlim(0, 3.7)
plt.ylim(bottom=0)

plt.tight_layout()

# Save figure
output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/HD_KH_fin/plots"
plt.savefig(os.path.join(output_dir, 'HD_sigma_vs_M.png'), dpi=300, bbox_inches='tight')
