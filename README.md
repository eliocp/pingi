# pingi: an easily and highly configurable data science plotter

Pingi is python wrapper around [Matplotlib](https://matplotlib.org/),
[Seaborn](https://seaborn.pydata.org/) and [IPython](https://ipython.org/) for creating
highly configurable data science visualizations with minimal code.

## Installation

### Using [`pip`](https://pypi.org/project/pip/)

* Install the latest stable release (and required dependencies) from
[PyPI](https://pypi.org/) using [`pip`](https://pypi.org/project/pip/) command:

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
the additional required dependencies using the command:

    ```bash
    pingi-install-latex
    ```
    and enabling the rendering in the Python code, using parameter `usetex=True` in
    function [`configure_rc()`](src/pingi/configure.py#L8):

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

### Build the package

* Build the package:

    ```bash
    uv build
    ```