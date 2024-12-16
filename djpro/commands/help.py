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
        Fore.GREEN,
    )

    log_with_color(
        logging.INFO,
        "\nAvailable subcommands:",
        Fore.WHITE,
    )

    # project
    log_with_color(
        logging.INFO,
        "\n  project            Creates a Django project with a scalable and modular architecture.",
        Fore.YELLOW,
        delay=0,
    )

    log_with_color(
        logging.INFO,
        "  Options:",
        Fore.WHITE,
        delay=0,
    )

    log_with_color(
        logging.INFO,
        "    --api              Includes basic configuration for an API (Django REST Framework).",
        Fore.BLUE,
        delay=0,
    )
    log_with_color(
        logging.INFO,
        "    --docker           Adds Docker configuration for easy deployment.",
        Fore.BLUE,
        delay=0,
    )
    log_with_color(
        logging.INFO,
        "    --unfold           Adds Unfold custom theme to Django admin site.",
        Fore.BLUE,
        delay=0,
    )

    # module
    log_with_color(
        logging.INFO,
        "\n  module             Creates a new module in your current project.",
        Fore.YELLOW,
        delay=0,
    )

    log_with_color(
        logging.INFO,
        "  Options:",
        Fore.WHITE,
        delay=0,
    )

    log_with_color(
        logging.INFO,
        "    -models            Include models.py file.",
        Fore.BLUE,
        delay=0,
    )
    log_with_color(
        logging.INFO,
        "    -views             Include views.py file",
        Fore.BLUE,
        delay=0,
    )
    log_with_color(
        logging.INFO,
        "    -serializers       Include serializers.py file.",
        Fore.BLUE,
        delay=0,
    )
    log_with_color(
        logging.INFO,
        "    -urls              Include urls.py file",
        Fore.BLUE,
        delay=0,
    )
    log_with_color(
        logging.INFO,
        "    -forms             Include forms.py file",
        Fore.BLUE,
        delay=0,
    )

    # man
    log_with_color(
        logging.INFO,
        "\n  man                Run manage.py commands easier.",
        Fore.YELLOW,
        delay=0,
    )
    log_with_color(
        logging.INFO,
        "  djpro man <command>",
        Fore.GREEN,
    )
    log_with_color(
        logging.INFO,
        "\n  Examples of use:",
        Fore.WHITE,
        delay=0,
    )
    log_with_color(
        logging.INFO,
        "    djpro man help     View list of available manage.py commands.",
        Fore.BLUE,
        delay=0,
    )
    log_with_color(
        logging.INFO,
        "    djpro man runserver",
        Fore.BLUE,
        delay=0,
    )
    log_with_color(
        logging.INFO,
        "    djpro man makemigrations",
        Fore.BLUE,
        delay=0,
    )
    log_with_color(
        logging.INFO,
        "    djpro man migrate\n",
        Fore.BLUE,
        delay=0,
    )


def man_help():
    log_with_color(
        logging.INFO,
        "\nCommand help guide:",
        Fore.GREEN,
        delay=1,
    )

    log_with_color(
        logging.INFO,
        "\nAvailable subcommands:",
        Fore.WHITE,
    )

    log_with_color(
        logging.INFO,
        "\n[auth]",
        Fore.YELLOW,
        delay=0,
    )

    log_with_color(
        logging.INFO,
        "  changepassword\n  createsuperuser",
        Fore.WHITE,
        delay=0,
    )

    log_with_color(
        logging.INFO,
        "\n[contenttypes]",
        Fore.YELLOW,
        delay=0,
    )

    log_with_color(
        logging.INFO,
        "  remove_stale_contenttypes",
        Fore.WHITE,
        delay=0,
    )

    log_with_color(
        logging.INFO,
        "\n[django]",
        Fore.YELLOW,
        delay=0,
    )

    log_with_color(
        logging.INFO,
        "  check\n  compilemessages\n  createcachetable\n  dbshell\n  diffsettings\n  dumpdata\n  flush\n  inspectdb\n  loaddata\n  makemessages\n  makemigrations\n  migrate\n  optimizemigration\n  sendtestemail\n  shell\n  showmigrations\n  sqlflush\n  sqlmigrate\n  sqlsequencereset\n  squashmigrations\n  startapp\n  startproject\n  test\n  testserver\n",
        Fore.WHITE,
        delay=0,
    )

    log_with_color(
        logging.INFO,
        "\n[sessions]",
        Fore.YELLOW,
        delay=0,
    )

    log_with_color(
        logging.INFO,
        "  clearsessions",
        Fore.WHITE,
        delay=0,
    )

    log_with_color(
        logging.INFO,
        "\n[staticfiles]",
        Fore.YELLOW,
        delay=0,
    )

    log_with_color(
        logging.INFO,
        "  collectstatic\n  findstatic\n  runserver",
        Fore.WHITE,
        delay=0,
    )
