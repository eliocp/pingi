#!/usr/bin/env bash

# ---> Get absolute path to scripts directory
SCRIPTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# ---> Get utility functions
source "$SCRIPTS_DIR/utils.sh" || return 1

# ----> Install latex
info "Updating package metadata from source..."
if sudo apt update; then
    info "Done."
else
    error "Failed."
fi

info "Installing LaTeX packages..."
# NOTE: sudo apt install does nothing if packages are already installed and up-to-date.
if sudo apt install -y \
    dvipng \
    texlive-latex-extra \
    texlive-fonts-recommended \
    cm-super; then
    info "Done."
else
    error "Failed."
fi
