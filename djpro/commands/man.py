import subprocess

from ..utils.logging import logging, log_with_color, Fore
from .help import man_help


def man(command: str):
    if command == "help":
        return man_help()

    try:
        subprocess.run(
            ["python", "src/bin/manage.py", command],
            text=True,
            check=True,
        )

    except subprocess.CalledProcessError:
        log_with_color(
            logging.INFO,
            "\nError while running the command.",
            Fore.RED,
        )


def run(args):
    """Entry point for command 'man'."""

    try:
        man(
            command=args.man_command,
        )

    except Exception as e:
        log_with_color(
            logging.INFO,
            f"\nError while running commands: {e}",
            Fore.RED,
        )
