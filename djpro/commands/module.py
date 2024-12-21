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

    new_module_dir = [
        modules_dir / module_name,
        modules_dir / module_name / "models",
        modules_dir / module_name / "views",
        modules_dir / module_name / "serializers",
    ]

    if new_module_dir[0].exists():
        raise FileExistsError(
            log_with_color(
                logging.INFO,
                f"\nThe module '{module_name}' already exists.",
                Fore.YELLOW,
            )
        )

    files = [
        new_module_dir[0] / "__init__.py",
        new_module_dir[1] / "__init__.py",
        new_module_dir[2] / "__init__.py",
        new_module_dir[3] / "__init__.py",
    ]

    file_mapping = {
        "models": (new_module_dir[1], "models.py"),
        "views": (new_module_dir[2], "views.py"),
        "serializers": (new_module_dir[3], "serializers.py"),
        "urls": (new_module_dir[0], "urls.py"),
        "forms": (new_module_dir[0], "forms.py"),
        "admin": (new_module_dir[0], "admin.py"),
        "apps": (new_module_dir[0], "apps.py"),
    }

    if args:
        files.extend(
            directory / filename
            for key, (directory, filename) in file_mapping.items()
            if getattr(args, key, False)
        )

    create_dirs(new_module_dir)
    create_files(files)


def run(args):
    """Entry point for command 'module'."""

    try:
        create_module(
            base_dir=args.base_dir,
            module_name=args.module_name,
            args=args,
        )

    except Exception as e:
        error_message = "\nError while creating module"
        if f"{e}" != "None":
            error_message += f": {e}"

        log_with_color(
            logging.INFO,
            error_message,
            Fore.RED,
        )
