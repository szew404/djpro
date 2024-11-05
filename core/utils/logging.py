import logging
import time

from colorama import Fore, Style, init

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(message)s")
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)

init(autoreset=True)


def log_with_color(level, message, color, delay=0):
    colored_message = f"{color}{message}{Style.RESET_ALL}"
    logger.log(level, colored_message)
    time.sleep(delay)
