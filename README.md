# pingi: an easily highly configurable data science plotter

Pingi is python wrapper around [Matplotlib](https://matplotlib.org/),
[Seaborn](https://seaborn.pydata.org/) and [IPython](https://ipython.org/) for creating
highly configurable data science visualizations with minimal code.

## Installation

### Using [`pip`](https://pypi.org/project/pip/)

The latest stable release (and required dependencies) can be installed from
[PyPI](https://pypi.org/) using [`pip`](https://pypi.org/project/pip/)
command:

```bash
pip install pingi
```

### Using [`uv`](https://docs.astral.sh/uv/)

Or, using [`uv`](https://docs.astral.sh/uv/) command:

```bash
uv add pingi
```

## Getting started

#### Use LaTeX text rendering

 One may integrate [LaTeX](https://www.latex-project.org/) in the plots by firstly
 installing the additional required dependencies using the command:
 
```bash
pingi-install-latex
```
and enabling the rendering in the Python code, using parameter `usetex=True` in function
[`configure_rc()`](src/pingi/configure.py#L8):

```python
from pingi.configure import configure_rc

configure_rc(usetex=True)
```

## Documentation


* [Examples gallery](https://eliocp.github.io/pingi/examples)


## Development

Create the development Python environment using all dependency groups:

```bash
uv sync --all-groups
```

Build the package:

```bash
uv build
```

Use [`ruff`](https://docs.astral.sh/ruff/) for Python linting and formatting:

```bash
ruff check .
ruff format .
```
