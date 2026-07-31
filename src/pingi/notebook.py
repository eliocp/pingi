from IPython.display import HTML, Markdown, display


def adjust_notebook_widget_style() -> None:
    """
    Adjust the styling of Jupyter Notebook widgets (e.g. `tqdm.notebook` progress bars)
    so that they match the VS Code theme. Run this very function in a notebook Python
    cell to apply the styling.

    The function injects CSS into the notebook to:
    * make widget output backgrounds transparent.
    * sync widget text color and font size with VS Code theme variables.

    Useful when working in VS Code notebooks to ensure consistent styling.

    Fore more details, see this [Stack Overflow
    answer](https://stackoverflow.com/a/77566731/4382986).
    """

    css = """
    <style>
    .cell-output-ipywidget-background {
        background-color: transparent !important;
    }
    :root {
        --jp-widgets-color: var(--vscode-editor-foreground);
        --jp-widgets-font-size: var(--vscode-editor-font-size);
    }  
    </style>
    """
    display(HTML(css))


def display_caption(caption: str = "") -> None:
    """
    Display Markdown-formatted caption.

    Parameters
    ----------
    caption : str, default=''
        Caption content to display.

    """
    display(
        Markdown(f"""
<span style="
    display: inline-block;
    font-size: 16px;
    font-weight: bold;
    font-style: italic;
    text-align: left;
    padding-top: 15pt;
    padding-left: 15pt;
">
{caption}
</span>
            """)
    )
