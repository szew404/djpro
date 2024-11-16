from ..logging import logging, log_with_color, Fore


def run_dev_messages():
    """Messages"""

    # Mensaje principal
    log_with_color(
        logging.INFO,
        "Your development environment is almost ready to run...",
        Fore.WHITE,
    )
    log_with_color(
        logging.INFO,
        "Run the following commands inside the folder 'src' of your project:\n",
        Fore.WHITE,
    )

    commands = [
        "pip install -r requirements.txt",
        "python bin/manage.py collectstatic",
        "python bin/manage.py runserver\n",
    ]

    for command in commands:
        log_with_color(logging.INFO, f"     {command}", Fore.WHITE)
