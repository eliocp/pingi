#!/usr/bin/env bash

# Exit on error (-e), on use of undefined variables (-u), and if any command in a
# pipeline fails (-o pipefail).
# For details, see: https://linuxcommand.org/lc3_man_pages/seth.html
set -euo pipefail


# ---> Get helpful paths
WORKING_DIR="$PWD"
# Get absolute path to this very script
SCRIPT_FILE="$(realpath "${BASH_SOURCE[0]}")"
# Get absolute path to parent directory of this very script (install)
INSTALL_DIR="$(dirname "$SCRIPT_FILE")"
# Get absolute path to parent directory of the install directory (scripts)
SCRIPTS_DIR="$(dirname "$INSTALL_DIR")"

# ---> Get functions for printing info, warning and error messages
source "$SCRIPTS_DIR/utils/print.sh"

# ----> Install latex
info "Updating package metadata from source..."
sudo apt update
info "Done."

info "Installing LaTeX packages..."
# NOTE: sudo apt install does nothing if packages are already installed and up-to-date.
sudo apt install -y \
    dvipng \
    texlive-latex-extra \
    texlive-fonts-recommended \
    cm-super
info "Done."
