from typing import Any, Literal, cast

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.axes import Axes
from matplotlib.container import BarContainer

from pingi.default import DefaultParams


def plot(
    ax: plt.Axes,  # type: ignore
    kind: str = "countplot",
    print_bar_label: bool = True,
    xmin: float | None = None,
    xmax: float | None = None,
    xlabel: str | None = None,
    xlabelpad: float | None = None,
    transform_xticklabels: str | None = None,
    xticklabels_rotation: float | None = None,
    xticklabels_ha: Literal["left", "center", "right"] = "center",
    xticklabels_fontsize: float | None = None,
    xmargin: float | None = None,
    ymin: float | None = None,
    ymax: float | None = None,
    ylabel: str | None = None,
    ylabelpad: float | None = None,
    yticklabels_fontsize: float | None = None,
    ymargin: float | None = None,
    fontsize_factor: float | None = None,
    minorticks_on: bool = False,
    plot_xgrid: bool = False,
    plot_ygrid: bool = False,
    aspect: Literal["auto", "equal"] | float | None = None,
    transform_legend_labels: str | None = None,
    bar_label_kwargs: dict[str, Any] | None = None,
    title_kwargs: dict[str, Any] | None = None,
    legend_kwargs: dict[str, Any] | None = None,
    **sns_kwargs: Any,
) -> None:
    """
    Add seaborn-based plot of kind `kind` with additional customisation to given axes
    `ax`.

    Parameters
    ----------
    ax : plt.Axes
        Plot axes.

    kind : str, default="countplot"
        The kind of seaborn plot (`"countplot"`, `"histplot"`, ...)

    print_bar_label : bool, default=True
        `True` to print bar labels (if `kind` corresponds to `"countplot"`, `"histplot"`
        or `"barplot"`). `False` to not.

    xmin : float or None, default=None
        Minimum value of the x-axis. If not defined, the default one from seaborn is
        used.

    xmax : float or None, default=None
        Maximum value of the x-axis. If not defined, the default one from seaborn is
        used.

    xlabel : str or None, default=None
        Label of the x-axis. If not defined, the default one from seaborn is used.

    xlabelpad : float or None, default=None
        Spacing in points from the x-axis bounding box including ticks and tick labels.
        If not defined, the default one from seaborn is used.

    transform_xticklabels : str or None, default=None
        The name of a string method for transforming the x-axis tick labels (e.g.
        `"capitalize"`, `"upper"`, `"lower"` ...). If not issued, no transformation is
        considered.

    xticklabels_rotation : float or None, default=None
        Rotation of the x-axis tick labels in degrees. If not defined, the default one
        from seaborn is used.

    xticklabels_ha : {"left", "center", "right"}, default="center"
        Horizontal alignment of the x-axis tick labels.

    xticklabels_fontsize : float or None, default=None
        Fontsize of the y-axis tick labels. If not defined, it is set as `9` scaled by
        `fontsize_factor`.

    xmargin : float or None, default=None
        Margin value for the x-axis (fraction of the x axis used as both left and right
        margins between the data and the axis limits). If not defined, the default one
        from seaborn is used.

    ymin : float or None, default=None
        Margin value for the y-axis (fraction of the y axis used as both top and bottom
        margins between the data and the axis limits). If not defined, the default one
        from seaborn is used.

    ymax : float or None, default=None
        Maximum value of the y-axis. If not defined, the default one from seaborn is
        used.

    ylabel : str or None, default=None
        Label of the y-axis. If not defined, the default one from seaborn is used.

    ylabelpad : float or None, default=None
        Spacing in points from the y-axis bounding box including ticks and tick labels.
        If not defined, the default one from seaborn is used.

    yticklabels_fontsize : float or None, default=None
        Fontsize of the x-axis tick labels. If not defined, it is set as `9` scaled by
        `fontsize_factor`.

    ymargin : float or None, default=None
        Margin value for the y-axis. If not defined, the default one from seaborn is
        used.

    fontsize_factor : float, default=DefaultParams.fontsize_factor
        A multiplication factor for the size of all fonts in the plot.

    minorticks_on : bool, default=False,
        Whether to plot axes' minor ticks between major ticks.

    plot_xgrid : bool, default=False
        Whether to plot or not an x-axis grid. Only used if `kind` does not correspond
        to `"heatmap"`.

    plot_ygrid : bool, default=False
        Whether to plot or not an y-axis grid. Only used if `kind` does not correspond
        to `"heatmap"`.

    aspect : {"auto", "equal"} or float or None, default=None
        Aspect ratio of the plot. If not defined, the default one from seaborn is used.

    transform_legend_labels : str or None, default=None
        The name of a string method for transforming the legend labels (e.g.
        `"capitalize"`, `"upper"`, `"lower"` ...). If not issued, no transformation is
        considered.

    bar_label_kwargs :  dict[str, Any] or None, default=None
        Bar label keyword arguments except container.

    title_kwargs : dict[str, Any] or None, default=None
        Title keyword arguments.

    legend_kwargs : dict[str, Any] or None, default=None
        Legend keyword arguments except `handles` and `labels`.

    sns_kwargs :
        Keyword arguments of the seaborn's base plotter.

    Returns
    -------
    None
        This function does not return anything. It draws in the given plot axes without
        showing it.

    """

    # Handle fontsize factor parameter
    fontsize_factor = (
        fontsize_factor
        if fontsize_factor is not None
        else DefaultParams.get_fontsize_factor()
    )

    # Set title
    if title_kwargs is not None:
        ax.set_title(
            fontsize=(
                title_kwargs["fontsize"]
                if title_kwargs is not None and "fontsize" in title_kwargs
                else 12 * fontsize_factor
            ),
            **(
                {k: v for k, v in title_kwargs.items() if k not in ["fontsize"]}
                if title_kwargs is not None
                else {}
            ),
        )

    # Handle seaborn's kwargs arguments
    sns_kwargs["ax"] = ax

    # Select seaborn plotter from kind
    plotter = getattr(sns, kind, None)

    # Raise error in case of kind not being supported
    if plotter is None:
        raise ValueError(f"There is no plotter of type {kind!r} in seaborn.")

    # Create seaborn's base plot
    plotter(**sns_kwargs)

    if kind in ["countplot", "histplot", "barplot"] and print_bar_label is True:
        # Print values above bars
        for container in ax.containers:  # type: ignore
            ax.bar_label(
                container=cast(BarContainer, container),
                fontsize=(
                    bar_label_kwargs["fontsize"]
                    if bar_label_kwargs is not None and "fontsize" in bar_label_kwargs
                    else 10 * fontsize_factor
                ),
                **(
                    {k: v for k, v in bar_label_kwargs.items() if k not in ["fontsize"]}
                    if bar_label_kwargs is not None
                    else {}
                ),
            )

        # Increase the y axes upper limit to accommodate the bar labels
        ax.set_ylim(top=1.2 * ax.get_ylim()[1])

    # Set axes limits
    if xmin is not None or xmax is not None:
        ax.set_xlim(xmin, xmax)  # type: ignore
    if ymin is not None or ymax is not None:
        ax.set_ylim(ymin, ymax)  # type: ignore

    # Define axes labels
    if xlabel is not None:
        ax.set_xlabel(
            xlabel,
            fontdict={"fontsize": 10 * fontsize_factor},
            labelpad=xlabelpad,  # type: ignore
        )
    if ylabel is not None:
        ax.set_ylabel(
            ylabel,
            fontdict={"fontsize": 10 * fontsize_factor},
            labelpad=ylabelpad,  # type: ignore
        )

    # If wanted, transform x-axis tick labels
    if transform_xticklabels is not None:
        ax.set_xticklabels(
            [
                getattr(label.get_text(), transform_xticklabels)()
                for label in ax.get_xticklabels()
            ]
        )

    # Set rotation, horizontal alignment of x-axis tick labels
    for label in ax.get_xticklabels():
        if xticklabels_rotation is not None:
            label.set_rotation(xticklabels_rotation)
        label.set_horizontalalignment(xticklabels_ha)

    # Set axes ticklabels size
    ax.tick_params(
        axis="x",
        labelsize=(
            xticklabels_fontsize
            if xticklabels_fontsize is not None
            else 9 * fontsize_factor
        ),
    )
    ax.tick_params(
        axis="y",
        labelsize=(
            yticklabels_fontsize
            if yticklabels_fontsize is not None
            else 9 * fontsize_factor
        ),
    )

    # Set axes' margins
    if xmargin is not None or ymargin is not None:
        ax.margins(x=xmargin, y=ymargin)  # type: ignore

    # Plot legend
    legend = ax.get_legend()  # Get default legend
    if legend is not None and (
        transform_legend_labels is not None or legend_kwargs is not None
    ):
        # Get default legend handles and labels
        handles = legend.legend_handles  # type: ignore
        labels = [text.get_text() for text in legend.get_texts()]

        if transform_legend_labels is not None:
            # Transform legend labels
            labels = [getattr(label, transform_legend_labels)() for label in labels]

        # Redefine legend
        ax.legend(
            handles=handles,
            labels=labels,
            title=(
                legend_kwargs["title"]
                if legend_kwargs is not None and "title" in legend_kwargs
                else legend.get_title().get_text()
            ),
            title_fontsize=(
                legend_kwargs["title_fontsize"]
                if legend_kwargs is not None and "title_fontsize" in legend_kwargs
                else 9 * fontsize_factor
            ),
            fontsize=(
                legend_kwargs["fontsize"]
                if legend_kwargs is not None and "fontsize" in legend_kwargs
                else 8 * fontsize_factor
            ),
            **(
                {
                    k: v
                    for k, v in legend_kwargs.items()
                    if k not in ["title", "title_fontsize", "fontsize"]
                }
                if legend_kwargs is not None
                else {}
            ),
        )

    # Set axes' minor ticks
    if minorticks_on is True:
        ax.minorticks_on()

    # Define x-axis grids
    if plot_xgrid is True and kind != "heatmap":
        # Define x-axis major grid
        ax.grid(
            axis="x",
            visible=True,
            which="major",
            color="lightgray",
            linestyle="solid",
            linewidth=0.5,
        )

        if minorticks_on is True:
            # Define x-axis minor grid
            ax.grid(
                axis="x",
                visible=True,
                which="minor",
                color="lightgray",
                linestyle="dotted",
                linewidth=0.5,
            )

    # Define y-axis grids
    if plot_ygrid is True and kind != "heatmap":
        # Define y_axis major grid
        ax.grid(
            axis="y",
            visible=True,
            which="major",
            color="lightgray",
            linestyle="solid",
            linewidth=0.5,
        )

        if minorticks_on is True:
            # Define y-axis minor grid
            ax.grid(
                axis="y",
                visible=True,
                which="minor",
                color="lightgray",
                linestyle="dotted",
                linewidth=0.5,
            )

    # Set plot aspect ratio
    if aspect is not None:
        ax.set_aspect(aspect)


def plot_diagonal(
    ax: Axes,
    **axline_kwargs: Any,
) -> None:
    """
    Add diagonal line (that is, a line of slope `1` that passes through origin) to plot
    of axes `ax` using pyplot's `ax.axline(xy1=(0, 0), slope=1, **axline_kwargs)`.

    Parameters
    ----------
    ax : plt.Axes
        Plot axes.

    axline_kwargs :
        Keyword arguments of pyplot's `axline()` except `xy1` and `slope`.

    Returns
    -------
    None
        This function does not return anything. It draws in the given plot axes without
        showing it.
    """

    ax.axline(
        xy1=(0, 0),
        slope=1,
        color=(
            axline_kwargs["color"]
            if axline_kwargs is not None and "color" in axline_kwargs
            else "black"
        ),
        linewidth=(
            axline_kwargs["linewidth"]
            if axline_kwargs is not None and "linewidth" in axline_kwargs
            else 0.75
        ),
        linestyle=(
            axline_kwargs["linestyle"]
            if axline_kwargs is not None and "linestyle" in axline_kwargs
            else "solid"
        ),
        alpha=(
            axline_kwargs["alpha"]
            if axline_kwargs is not None and "alpha" in axline_kwargs
            else 0.75
        ),
        zorder=(
            axline_kwargs["zorder"]
            if axline_kwargs is not None and "zorder" in axline_kwargs
            else 1
        ),
        **(
            {
                k: v
                for k, v in axline_kwargs.items()
                if k not in ["color", "linewidth", "linestyle", "alpha", "zorder"]
            }
            if axline_kwargs is not None
            else {}
        ),
    )
