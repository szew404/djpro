from django.core.management.utils import get_random_secret_key


def generate_secret_key():
    """Django predefined function to create the Django secret key"""
    return get_random_secret_key()
