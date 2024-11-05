import os
import argparse

from .commands.logging import logging, log_with_color, Fore
from .commands.write_config import write
from .commands.create import create_directories, create_files


def help():
    log_with_color(
        logging.INFO,
        "\nType 'dj-pro help <subcommand>' for help on a specific subcommand.",
        Fore.WHITE,
        delay=1,
    )

    log_with_color(
        logging.INFO,
        "\n  dj-pro <subcommand> [options]",
        Fore.BLUE,
        delay=1,
    )

    log_with_color(
        logging.INFO,
        "\nAvailable subcommands:",
        Fore.WHITE,
        delay=1,
    )

    log_with_color(
        logging.INFO,
        "\n[dj-pro]",
        Fore.BLUE,
        delay=1,
    )

    log_with_color(
        logging.INFO,
        "\n  new        Create a Django project with a scalable and modular architecture.",
        Fore.BLUE,
        delay=1,
    )

    log_with_color(
        logging.INFO,
        "  Options:",
        Fore.WHITE,
    )

    log_with_color(
        logging.INFO,
        "    --api      Includes basic configuration for an API (Django REST Framework).",
        Fore.BLUE,
        delay=0.5,
    )
    log_with_color(
        logging.INFO,
        "    --docker       Add Docker configuration.",
        Fore.BLUE,
        delay=0.5,
    )
    log_with_color(
        logging.INFO,
        "    --unfold       Add Django Admin Site customization.",
        Fore.BLUE,
        delay=0.5,
    )


def create_project():
    base_dir = os.path.join(os.getcwd(), "src")
    parser = argparse.ArgumentParser(description="Create a Django project structure.")
    parser.add_argument("project_name", type=str, help="Name of your Django project.")
    parser.add_argument(
        "--api", action="store_true", help="Setup the project to include an API."
    )

    args = parser.parse_args()
    project_name = args.project_name

    if args.api:
        api = True

    log_with_color(logging.INFO, "Running commands...", Fore.BLUE, delay=2)

    create_directories(base_dir, api)  # Create folders
    log_with_color(logging.INFO, "---- Directories created successfully.", Fore.GREEN)

    create_files(base_dir, api)  # Create files
    write(base_dir, project_name, api)  # Write files
    log_with_color(logging.INFO, "---- Files created successfully.", Fore.GREEN)

    log_with_color(
        logging.INFO, f"Project '{project_name}' created successfully!", Fore.BLUE
    )

    log_with_color(
        logging.INFO,
        "\nRun your Django project using: python bin/manage.py runserver",
        Fore.WHITE,
    )
