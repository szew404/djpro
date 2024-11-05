from ..utils.logging import logging, log_with_color, Fore


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
