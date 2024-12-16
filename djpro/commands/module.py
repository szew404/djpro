# This file is part of djpro.
#
# Copyright (c) 2024, Franco Gidaszewski <gidaszewskifranco@gmail.com>
#
# For the full copyright and license information, please view
# the LICENSE.txt file that was distributed with this source code.

from pathlib import Path

from ..utils.logging import logging, log_with_color, Fore
from ..utils.write_and_config import create_dirs, create_files


def create_module(
    base_dir: Path,
    module_name: str,
    args: list[str] = None,
):
    """Function to create a new module in the current project"""

    base_dir_path = Path(base_dir)
    modules_dir = base_dir_path / "modules"

    if not modules_dir.exists():
        raise FileNotFoundError(
            log_with_color(
                logging.INFO,
                f"\nThe 'modules' directory does not exist in {base_dir_path}. \nRun this command in the root folder of your project.",
                Fore.YELLOW,
            )
        )

    new_module_dir = modules_dir / module_name

    if new_module_dir.exists():
        raise FileExistsError(
            log_with_color(
                logging.INFO,
                f"\nThe module '{module_name}' already exists.",
                Fore.YELLOW,
            )
        )

    files = [
        new_module_dir / "__init__.py",
    ]

    file_mapping = {
        "models": "models.py",
        "views": "views.py",
        "serializers": "serializers.py",
        "urls": "urls.py",
        "forms": "forms.py",
    }

    if args:
        files.extend(
            new_module_dir / filename
            for key, filename in file_mapping.items()
            if getattr(args, key, False)
        )

    create_dirs([new_module_dir])
    create_files(files)


def run(args):
    """Entry point for command 'module'."""

    try:
        create_module(
            base_dir=args.base_dir,
            module_name=args.module_name,
            args=args,
        )

    except Exception:
        return
