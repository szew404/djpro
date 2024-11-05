import os
from .logging import logging, log_with_color, Fore

from .content import (
    settings_content,
    settings_api,
    settings_base_content,
    settings_dev_content,
    settings_prod_content,
    wsgi_content,
    asgi_content,
    urls_content,
    env_content,
    requirements_content,
    requirements_api,
    gitignore_content,
    views_auth_content,
    urls_auth_content,
    manage_content,
)

from .django_utils import generate_secret_key


def write(base_dir: str, project_name: str, api: bool = False):
    """
    Write the content in each .py file

    Args:
        base_dir (str): Path to the project dir
        project_name (str): Project name
    """

    log_with_color(logging.INFO, "Configuring files...", Fore.YELLOW, delay=3)
    # requirements.txt
    with open(os.path.join("requirements.txt"), "w") as f:
        f.write(requirements_content)

    # settings.py
    with open(os.path.join(base_dir, "config", "settings.py"), "w") as f:
        f.write(settings_content.format(project_name=project_name))

    if api:
        # settings_base.py
        with open(os.path.join(base_dir, "config", "settings_base.py"), "w") as f:
            f.write(settings_api)

        # requirements.txt
        with open(os.path.join("requirements.txt"), "a") as f:
            f.write("\n")
            f.write(requirements_api)
    else:
        with open(os.path.join(base_dir, "config", "settings_base.py"), "w") as f:
            f.write(settings_base_content)

    # settings_dev.py
    with open(os.path.join(base_dir, "config", "settings_dev.py"), "w") as f:
        f.write(settings_dev_content)

    # settings_prod.py
    with open(os.path.join(base_dir, "config", "settings_prod.py"), "w") as f:
        f.write(settings_prod_content)

    # wsgi.py
    with open(os.path.join(base_dir, "config", "wsgi.py"), "w") as f:
        f.write(wsgi_content.format(project_name=project_name))

    # asgi.py
    with open(os.path.join(base_dir, "config", "asgi.py"), "w") as f:
        f.write(asgi_content.format(project_name=project_name))

    # urls.py
    with open(os.path.join(base_dir, "config", "urls.py"), "w") as f:
        f.write(urls_content.format(project_name=project_name))

    # bin/manage.py
    with open(os.path.join(base_dir, "bin", "manage.py"), "w") as f:
        f.write(manage_content)

    # auth/views.py
    with open(os.path.join(base_dir, "modules", "auth", "views.py"), "w") as f:
        f.write(views_auth_content)

    # auth/urls.py
    with open(os.path.join(base_dir, "modules", "auth", "urls.py"), "w") as f:
        f.write(urls_auth_content)

    # env
    with open(os.path.join(".env"), "w") as f:
        f.write(env_content.format(secret_key=generate_secret_key()))

    # gitignore
    with open(os.path.join(".gitignore"), "w") as f:
        f.write(gitignore_content)
