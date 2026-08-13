import subprocess
from importlib.resources import files


def install_latex() -> None:
    """
    Install LaTeX dependencies by running the installation script
    `scripts/install/install_latex.sh`.
    """
    # Path to latex installation script
    script = files("pingi").joinpath("scripts/install/install_latex.sh")
    # Run script
    subprocess.run(
        # Command arguments
        [
            "bash",
            "-c",
            f'source "{script}"',
        ],
        # Raise error if the command fails
        check=True,
    )


def uninstall_latex() -> None:
    """
    Uninstall LaTeX dependencies by running the uninstallation script
    `scripts/install/uninstall_latex.sh`.
    """
    # Path to latex installation script
    script = files("pingi").joinpath("scripts/install/uninstall_latex.sh")
    # Run script
    subprocess.run(
        # Command arguments
        [
            "bash",
            "-c",
            f'source "{script}"',
        ],
        # Raise error if the command fails
        check=True,
    )
