import shutil

import matplotlib.pyplot as plt

from pingi.default import DefaultParams


def configure_rc(
    axisbelow: bool = True,
    usetex: bool = False,
    font_family: str | None = None,
    dpi_display: float = 300.0,
    dpi_save: float = 300.0,
    fontsize_factor: float = 1.0,
) -> None:
    """
    Configure matplotlib pyplot and seaborn's RC (Runtime Configuration) by:
    - putting axes ticks and the gridlines below plots, if `axisbelow` is `True`;
    - using LaTeX, if `usetex` is `True`;
    - using issued family font (`font_family`);
    - setting default DPI (Dots Per Inch) of the figures when displaying to
    `dpi_display`.
    - setting default DPI (Dots Per Inch) of the figures when writing to file to
    `dpi_save`.
    - setting default multiplication factor for the size of all fonts considered by the
    visualization functions to `fontsize_factor`.

    Note that since seaborn uses matplotlib pyplot's RC, by setting the latter, one is
    also setting the RC of the former.

    The parameters of the runtime configuration are listed
    [here](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams).

    Parameters
    ----------
    axisbelow : bool, default=True
        Whether to put axes ticks and the gridlines below the plots.
    usetex : bool, default=False
        Whether to use LaTeX to render text.
    font_family : str or None, default=None
        Font family for text (e.g. `"serif"` for the case of the LaTeX family font). If
        not issued, the default one is used.
    dpi_display : float, default=300.0
        Figure's default DPI (Dots Per Inch) when displaying.
    dpi_save : float, default=300.0
        Figure's default DPI (Dots Per Inch) when writing to file.
    fontsize_factor : float, default=DefaultParams.fontsize_factor
        A multiplication factor for the size of all fonts considered in the visualizaton
        functions.

    Returns
    -------
    None

    """

    # Enable LaTeX only if available
    if usetex is True and shutil.which("latex") is None:
        raise RuntimeError(
            "LaTeX was requested (usetex=True), but no 'latex' executable was found"
            " on PATH. Install the required LaTeX dependencies by running:"
            "\npingi-install-latex"
        )

    # Put axes ticks and the gridlines below the plots if wanted
    plt.rc("axes", axisbelow=axisbelow)
    # Use LaTeX if wanted
    plt.rc("text", usetex=usetex)
    # Use issued family font for text
    # NOTE: LaTeX family font corresponds to "serif".
    if font_family is not None:
        plt.rcParams["font.family"] = font_family

    # Set default DPI (Dots Per Inch) of the figures when displaying
    # NOTE: https://stackoverflow.com/a/73706597/4382986
    plt.rcParams["figure.dpi"] = dpi_display
    # Set default DPI of the figures when writing to file
    plt.rcParams["savefig.dpi"] = dpi_save
    # Set default multiplication factor for the size of all fonts considered by the
    # visualization functions
    DefaultParams.set_fontsize_factor(fontsize_factor)
