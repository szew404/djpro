# This file is part of djpro.
#
# Copyright (c) 2024, Franco Gidaszewski <gidaszewskifranco@gmail.com>
#
# For the full copyright and license information, please view
# the LICENSE.txt file that was distributed with this source code.

from ..utils.logging import logging, log_with_color, Fore


def help():
    log_with_color(
        logging.INFO,
        "\nCommand help guide:",
        Fore.WHITE,
        delay=1,
    )

    log_with_color(
        logging.INFO,
        "\n  djpro <subcommand> [options]",
        Fore.BLUE,
    )

    log_with_color(
        logging.INFO,
        "\nAvailable subcommands:",
        Fore.WHITE,
    )

    log_with_color(
        logging.INFO,
        "\n  project          Creates a Django project with a scalable and modular architecture.",
        Fore.YELLOW,
        delay=0.5,
    )

    log_with_color(
        logging.INFO,
        "\n  Options:",
        Fore.WHITE,
        delay=0.3,
    )

    log_with_color(
        logging.INFO,
        "    --api          Includes basic configuration for an API (Django REST Framework).",
        Fore.BLUE,
        delay=0.2,
    )
    log_with_color(
        logging.INFO,
        "    --docker       Adds Docker configuration for easy deployment.",
        Fore.BLUE,
        delay=0.2,
    )
    log_with_color(
        logging.INFO,
        "    --unfold       Adds Unfold custom theme to Django admin site.",
        Fore.BLUE,
        delay=0.2,
    )

    log_with_color(
        logging.INFO,
        "\n  help          Displays the command help guide.",
        Fore.YELLOW,
        delay=0.5,
    )
