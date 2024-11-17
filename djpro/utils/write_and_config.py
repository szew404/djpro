# This file is part of djpro.
#
# Copyright (c) 2024, Franco Gidaszewski <gidaszewskifranco@gmail.com>
#
# For the full copyright and license information, please view
# the LICENSE.txt file that was distributed with this source code.

from pathlib import Path
from ..utils.logging import logging, log_with_color, Fore

from .files_content import (
    settings_api,
    settings_unfold,
    settings_api_unfold,
    settings_base_content,
    requirements_api,
    requirements_unfold,
)


def create_dirs(dirs: list[Path]):
    """Function to create folders"""
    for dir in dirs:
        dir.mkdir(parents=True, exist_ok=True)


def create_files(files: list[Path]):
    """Function to create files."""
    for file_path in files:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch()


def write_to_file(file_path: Path, content: str, mode: str = "w"):
    """Function to write content."""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, mode) as f:
        f.write(content)


def configure_requirements(api: bool, unfold: bool) -> str:
    """Config requirements content"""
    requirements = []
    if api:
        requirements.append(requirements_api)
    if unfold:
        requirements.append(requirements_unfold)
    return "".join(requirements)


def configure_settings_base(api: bool, unfold: bool) -> str:
    """Config settings content"""

    if api and unfold:
        log_with_color(
            logging.INFO,
            "\nConfiguring Unfold...",
            Fore.WHITE,
            delay=3,
        )
        return settings_api_unfold

    if api:
        return settings_api

    if unfold:
        log_with_color(
            logging.INFO,
            "\nConfiguring Unfold...",
            Fore.WHITE,
            delay=2,
        )
        return settings_unfold

    return settings_base_content  # Default
