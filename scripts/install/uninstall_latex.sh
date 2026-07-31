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

# ---> Uninstall latex
info "Removing LaTeX packages..."
sudo apt remove --purge -y \
    dvipng \
    texlive-latex-extra \
    texlive-fonts-recommended \
    cm-super
info "Done."

info "Removing unused dependencies..."
sudo apt autoremove -y
info "Done."

info "Cleaning package cache..."
sudo apt clean
info "Done."