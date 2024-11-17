from ..logging import logging, log_with_color, Fore


def run_prod_messages():
    """Messages"""

    # Mensajes principales
    messages = [
        "Your production environment is almost ready to run...",
        "Learn how to setup and run your production environment using Docker Compose:\n",
        "https://djpro.readthedocs.io/en/latest/quickstart.html#including-docker-configuration\n",
    ]

    for message in messages:
        log_with_color(logging.INFO, message, Fore.WHITE)
