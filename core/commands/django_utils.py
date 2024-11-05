from django.core.management.utils import get_random_secret_key


def generate_secret_key():
    return get_random_secret_key()
