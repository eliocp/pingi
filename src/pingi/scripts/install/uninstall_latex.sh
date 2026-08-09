#!/usr/bin/env bash

# ---> Get absolute path to scripts directory
SCRIPTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# ---> Get utility functions
source "$SCRIPTS_DIR/utils.sh"

# ---> Uninstall latex
info "Removing LaTeX packages..."
if sudo apt remove --purge -y \
    dvipng \
    texlive-latex-extra \
    texlive-fonts-recommended \
    cm-super; then
    info "Done."
else
    error "Failed."
fi

info "Removing unused dependencies..."
if sudo apt autoremove -y; then
    info "Done."
else
    error "Failed."
fi

info "Cleaning package cache..."
if sudo apt clean; then
    info "Done."
else
    error "Failed."
fi