import numpy as np
import matplotlib.pyplot as plt
import os

# Mach numbers
M = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])

# Magnetic energy amplification factors
amp_001 = [
    1.19303971, 1.6794872, 2.1793854,
    2.2873498, 4.0457193, 3.3782528
]

amp_005 = [
    1.0000000000787468, 1.13039178, 1.28247636,
    1.26827104, 1.25229256, 1.28038992
]

amp_01 = [
    1.0000010000006876, 1.02605977, 1.12729406,
    1.15234012, 1.13616416, 1.114441694
]

# Plot
plt.figure(figsize=(8, 5.5))

plt.plot(
    M, amp_001,
    color="royalblue", marker="o", linestyle="-",
    linewidth=2, markersize=6,
    label=r"$\sigma_{\mathrm{pol}} = 0.01$"
)

plt.plot(
    M, amp_005,
    color="darkorange", marker="s", linestyle="--",
    linewidth=2, markersize=6,
    label=r"$\sigma_{\mathrm{pol}} = 0.05$"
)

plt.plot(
    M, amp_01,
    color="forestgreen", marker="^", linestyle="-.",
    linewidth=2, markersize=6,
    label=r"$\sigma_{\mathrm{pol}} = 0.1$"
)

# Labels and title
plt.xlabel(r"Mach number, $M$", fontsize=30, labelpad=10)
plt.ylabel(
    r"$E_{\mathrm{mag,max}}/E_{\mathrm{mag},0}$",
    fontsize=30,
    labelpad=20
)
plt.title(
    "Factors for Different M",
    fontsize=30,
    pad=17
)

# Formatting
plt.legend(fontsize=20)
plt.grid(True, linestyle=":", alpha=0.7)
plt.xticks(M)
plt.xlim(0.3, 3.2)
plt.ylim(bottom=0)
plt.tick_params(axis="both", labelsize=15)

plt.tight_layout()
output_dir = "/cephfs/store/astro-hl278/hc636/PLUTO_DATA/MHD_KH_par1/plots"
plt.savefig(os.path.join(output_dir, "MHD_KHI_amplification_vs_M.png"),
    dpi=300, bbox_inches="tight"
)
