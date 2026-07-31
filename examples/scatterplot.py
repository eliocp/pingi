"""Create a highly customized scatterplot."""

import matplotlib.pyplot as plt
import seaborn as sns

from pingi.configure import configure_rc
from pingi.plot import plot

# Configure matplotlib pyplot and seaborn's RC (Runtime Configuration)
configure_rc(
    axisbelow=True,
    usetex=False,
    font_family="serif",
    dpi_display=300.0,
    dpi_save=300.0,
    fontsize_factor=1.25,
)

# Initialize figure
plt.figure(figsize=(6.4, 4.8))
ax = plt.axes()

# Plot scatterplot
plot(
    ax=ax,
    kind="scatterplot",
    data=sns.load_dataset("penguins"),
    x="bill_depth_mm",
    y="flipper_length_mm",
    hue="species",
    palette="pastel",
    # Marker
    marker="o",
    edgecolor="black",
    linewidth=0.3,
    alpha=0.85,
    s=25,
    # Axes
    xlabel="Bill Depth [mm]",
    ylabel="Flipper Length [mm]",
    xlabelpad=10,
    ylabelpad=10,
    xmargin=0.05,
    ymargin=0.05,
    # Grid
    minorticks_on=True,
    plot_xgrid=True,
    plot_ygrid=True,
    # Title
    title_kwargs={
        "label": "Flipper Length vs Bill Depth",
        "pad": 10,
    },
    # Legend
    legend_kwargs={
        "title": "Species",
        "loc": "center left",
        "framealpha": 0,
        "handletextpad": 0.3,
        "labelspacing": 1.15,
        "bbox_to_anchor": (0.99, 0.5),
    },
)


# Save the figure with tight layout
plt.savefig("scatterplot.png", bbox_inches="tight")

# Show plot with tight layout
plt.tight_layout()
plt.show()
