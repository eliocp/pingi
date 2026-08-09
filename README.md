# **pingi**: an easily and highly configurable data science plotter

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
<!-- pre-commit usag: https://pre-commit.com/#badging-your-repository -->
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
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![uv](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FOnyx-Nostalgia%2Fuv%2Frefs%2Fheads%2Ffix%2Flogo-badge%2Fassets%2Fbadge%2Fv0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Hatch project](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pypa/hatch/master/docs/assets/badge/v0.json)](https://github.com/pypa/hatch)

[`pingi`](https://github.com/eliocp/pingi) is a python wrapper around
[`matplotlib`](https://matplotlib.org/), [`seaborn`](https://seaborn.pydata.org/) and
[`ipython`](https://ipython.org/) for creating highly configurable data science
visualizations with minimal code.

## Requirements

To be able to install and use the [pingi](https://github.com/eliocp/pingi)
package in your project, you would need:

* An [Unix](https://en.wikipedia.org/wiki/Unix)-like environment.
* [`uv`](https://docs.astral.sh/uv/) project manager.

## Installation

### 1. Install package from PyPI

* Install the latest stable release from [PyPI](https://pypi.org/project/pingi/) in the
activated virtual environment using [`uv`](https://docs.astral.sh/uv/):

    ```bash
    uv add pingi
    ```

### 2. Install LaTeX (optional)

* To further use [LaTeX](https://www.latex-project.org/) in the plots, install its dependencies:

    ```bash
    uv run pingi-install-latex
    ```


## Getting started

#### Use LaTeX text rendering

* Enabling LaTeX rendering in the plots by setting parameter `usetex=True` in function
[`configure_rc()`](https://github.com/eliocp/pingi/tree/main/src/pingi/configure.py#L8):

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
## Documentation

To be built.

## Contributing

If you are a project developer, please read
[CONTRIBUTING.md](https://github.com/eliocp/pingi/blob/main/CONTRIBUTING.md) to
assimilate the development workflow, build Docker images from the project source code
and locally run them.

## Releasing

If you are a project maintainer, please read
[RELEASING.md](https://github.com/eliocp/pingi/blob/main/RELEASING.md) to know how to
build and publish the package to [PyPI](https://pypi.org/) and to create [GitHub
releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
after successful merge pull requests.

## License

`pingi` is licensed under the terms of the [MIT
license](https://github.com/eliocp/pingi/blob/main/LICENSE). 