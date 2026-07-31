from typing import Any

from matplotlib.axes import Axes

from pingi.default import DefaultParams


def plot_score_text(
    ax: Axes,
    scores: dict[str, float],
    fmt: str = "%.2f",
    fontsize_factor: float | None = None,
    **text_kwargs: Any,
) -> None:
    """
    Annotate `scores` with format `fmt` and font size adjusted by `fontsize_factor` to a
    plot of axes `ax` using pyplot's `ax.text()`.

    Parameters
    ----------
    ax : plt.Axes
        Plot axes.

    scores : dict[str, float]
        A dictionary containing the scores to be printed.

    fmt : str, default="%.2f"
        Format of the score values.

    fontsize_factor : float, default=DefaultParams.fontsize_factor
        A multiplication factor for the font size of the annotation.

    text_kwargs :
        Keyword arguments of pyplot's `text()` method except `s`.

    Returns
    -------
    None
        This function does not return anything. It draws in the given plot axes without
        showing it.
    """

    fontsize_factor = (
        fontsize_factor
        if fontsize_factor is not None
        else DefaultParams.get_fontsize_factor()
    )

    ax.text(
        s="".join(
            [
                f"{score_label} $=$ " + f"${fmt % score_value}$" + "\n"
                for (score_label, score_value) in scores.items()
            ]
        ),
        x=(
            text_kwargs["x"] if text_kwargs is not None and "x" in text_kwargs else 0.03
        ),
        y=(
            text_kwargs["y"] if text_kwargs is not None and "y" in text_kwargs else 0.97
        ),
        transform=(
            text_kwargs["transform"]
            if text_kwargs is not None and "transform" in text_kwargs
            else ax.transAxes
        ),
        linespacing=(
            text_kwargs["linespacing"]
            if text_kwargs is not None and "linespacing" in text_kwargs
            else 1.5
        ),
        color=(
            text_kwargs["color"]
            if text_kwargs is not None and "color" in text_kwargs
            else "black"
        ),
        ha=(
            text_kwargs["ha"]
            if text_kwargs is not None and "ha" in text_kwargs
            else "left"
        ),
        va=(
            text_kwargs["va"]
            if text_kwargs is not None and "va" in text_kwargs
            else "top"
        ),
        fontsize=(
            text_kwargs["fontsize"]
            if text_kwargs is not None and "fontsize" in text_kwargs
            else 8 * fontsize_factor
        ),
        **(
            {
                k: v
                for k, v in text_kwargs.items()
                if k
                not in [
                    "x",
                    "y",
                    "transform",
                    "linespacing",
                    "color",
                    "ha",
                    "va",
                    "fontsize",
                ]
            }
            if text_kwargs is not None
            else {}
        ),
    )
