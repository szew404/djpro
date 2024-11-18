from django.core.management.utils import get_random_secret_key


def generate_secret_key():
    """Django predefined function to create the Django secret key.
    Return a 50 character random string usable as a SECRET_KEY setting value."""
    return get_random_secret_key()
