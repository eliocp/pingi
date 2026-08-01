# pingi: an easily and highly configurable data science plotter

<!-- Badges from [Shields.io](https://shields.io/badges) -->

<!-- ----------------------------- PyPI badges ----------------------------- -->
<!-- NOTE: the values of all PyPI badges are inferred from the PyPI website dedicated
to the project. All PyPI-related badges may be found
[here](https://shields.io/search/?q=pypi)-->
<!-- Packge version: https://shields.io/badges/py-pi-version -->
<!-- Pakage python version: https://shields.io/badges/py-pi-python-version -->
<!-- Package license: https://shields.io/badges/py-pi-license -->
<!-- Package implementation: https://shields.io/badges/py-pi-implementation -->
<!-- Package indicator for availability of wheel distribution : https://shields.io/badges/py-pi-wheel -->
<!-- Package development status: https://shields.io/badges/py-pi-status -->

<!-- ---------------------------- GitHub badges ---------------------------- -->
<!-- NOTE: the values of all GitHub badges are inferred from the GitHub repo of the
project. All GitHub-related badges may be found
[here](https://shields.io/search/?q=github)-->

<!-- GitHub time of last commit: https://shields.io/badges/git-hub-last-commit -->

<!-- ---------------------------- Other badges ----------------------------- -->
<!-- uv package and project manager usage: https://github.com/astral-sh/uv/pull/15075#issue-3291641128 -->
<!-- Ruff linter and formatter usage: https://github.com/astral-sh/ruff/blob/main/README.md?plain=1 -->
<!-- Hatch build backend usage: https://hatch.pypa.io/dev/next-steps/#community -->
![PyPI Version](https://img.shields.io/pypi/v/pingi)
![PyPI Python Version](https://img.shields.io/pypi/pyversions/pingi)
![PyPI License](https://img.shields.io/pypi/l/pingi)
![PyPI Implementation](https://img.shields.io/pypi/implementation/pingi)
![PyPI Wheel](https://img.shields.io/pypi/wheel/pingi)
![PyPI Status](https://img.shields.io/pypi/status/pingi)
![GitHub last commit](https://img.shields.io/github/last-commit/eliocp/pingi)
[![uv](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FOnyx-Nostalgia%2Fuv%2Frefs%2Fheads%2Ffix%2Flogo-badge%2Fassets%2Fbadge%2Fv0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Hatch project](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pypa/hatch/master/docs/assets/badge/v0.json)](https://github.com/pypa/hatch)

Pingi is a python wrapper around [Matplotlib](https://matplotlib.org/),
[Seaborn](https://seaborn.pydata.org/) and [IPython](https://ipython.org/) for creating
highly configurable data science visualizations with minimal code.

## Installation

### Using [`pip`](https://pypi.org/project/pip/)

* Install the latest stable release (and required dependencies) from
[PyPI](https://pypi.org/project/pingi/) using [`pip`](https://pypi.org/project/pip/)
command:

    ```bash
    pip install pingi
    ```

### Using [`uv`](https://docs.astral.sh/uv/)

* Or, using [`uv`](https://docs.astral.sh/uv/) command:

    ```bash
    uv add pingi
    ```

## Getting started

#### Use LaTeX text rendering

* Integrate [LaTeX](https://www.latex-project.org/) in the plots by firstly installing
the additional required dependencies using [`uv`](https://docs.astral.sh/uv/):

    ```bash
    uv run pingi-install-latex
    ```
    and enabling the rendering in the Python code, using parameter `usetex=True` in
    function [`configure_rc()`](https://github.com/eliocp/pingi/tree/main/src/pingi/configure.py#L8):

    ```python
    from pingi.configure import configure_rc

    configure_rc(usetex=True)
    ```

## Documentation

To be built.

## Development

### Installation of development dependencies

* Create the development environment using all dependency groups:

    ```bash
    uv sync --all-groups
    ```

### Linting

* Use [`ruff`](https://docs.astral.sh/ruff/linter/) for Python linting:

    ```bash
    uv run ruff check --fix --diff
    ```
    The command above will check for bugs, suspicious code, style violations, dead code,
    complexity issues and import problems. It will further proposed fixes.

* Apply the fixes:

    ```bash
    uv run ruff check --fix
    ```

### Formatting

* Use [`ruff`](https://docs.astral.sh/ruff/formatter/) for Python formatting:

    ```bash
    uv run ruff format --diff
    ```

    The command above will check the code structure, namely, the indentation, spaces,
    line breaks, quote style and long line wrapping. It will further show the proposed
    changes.

* Apply the changes:

    ```bash
    uv run ruff format
    ```

## License

Pingi is licensed under the terms of the [MIT
license](https://github.com/eliocp/pingi/blob/main/LICENSE). 