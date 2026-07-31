import subprocess
from pathlib import Path


def install_latex() -> None:
    """
    Install LaTeX dependencies by running the installation script
    `scripts/install/install_latex.sh`.
    """
    # Path to latex installation script
    script = (
        Path(__file__).resolve().parents[2] / "scripts" / "install" / "install_latex.sh"
    )
    # Run script
    subprocess.run(
        # Command arguments
        ["bash", str(script)],
        # Raise error if the command fails
        check=True,
    )


def uninstall_latex() -> None:
    """
    Uninstall LaTeX dependencies by running the uninstallation script
    `scripts/install/uninstall_latex.sh`.
    """
    # Path to latex installation script
    script = (
        Path(__file__).resolve().parents[2]
        / "scripts"
        / "install"
        / "uninstall_latex.sh"
    )
    # Run script
    subprocess.run(
        # Command arguments
        ["bash", str(script)],
        # Raise error if the command fails
        check=True,
    )
