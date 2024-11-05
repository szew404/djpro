import os
from .logging import logging, log_with_color, Fore


def create_directories(base_dir: str, api: bool = False):
    log_with_color(logging.INFO, "Creating directories...", Fore.BLUE)
    os.makedirs(os.path.join(base_dir, "bin"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "config"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "modules"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "modules", "auth"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "templates"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "static"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "utils"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "tests"), exist_ok=True)

    if api:
        os.makedirs(os.path.join(base_dir, "modules", "api"), exist_ok=True)


def create_files(base_dir: str, api: bool = False):
    log_with_color(logging.INFO, "Creating files...", Fore.BLUE)
    open(os.path.join(base_dir, "bin", "__init__.py"), "w").close()
    open(os.path.join(base_dir, "bin", "manage.py"), "w").close()
    open(os.path.join(base_dir, "config", "__init__.py"), "w").close()
    open(os.path.join(base_dir, "config", "settings_base.py"), "w").close()
    open(os.path.join(base_dir, "config", "settings_prod.py"), "w").close()
    open(os.path.join(base_dir, "config", "settings_dev.py"), "w").close()
    open(os.path.join(base_dir, "config", "asgi.py"), "w").close()
    open(os.path.join(base_dir, "config", "wsgi.py"), "w").close()
    open(os.path.join(base_dir, "config", "urls.py"), "w").close()
    open(os.path.join(base_dir, "modules", "__init__.py"), "w").close()
    open(os.path.join(base_dir, "modules", "auth", "__init__.py"), "w").close()
    open(os.path.join(base_dir, "modules", "auth", "views.py"), "w").close()
    open(os.path.join(base_dir, "modules", "auth", "urls.py"), "w").close()
    open(os.path.join(base_dir, "utils", "__init__.py"), "w").close()
    open(os.path.join(base_dir, "tests", "__init__.py"), "w").close()

    if api:
        open(os.path.join(base_dir, "modules", "api", "__init__.py"), "w").close()
        open(os.path.join(base_dir, "modules", "api", "serializers.py"), "w").close()
        open(os.path.join(base_dir, "modules", "api", "models.py"), "w").close()
        open(os.path.join(base_dir, "modules", "api", "views.py"), "w").close()
        open(os.path.join(base_dir, "modules", "api", "urls.py"), "w").close()

    open(os.path.join(os.getcwd(), ".gitignore"), "w").close()
    open(os.path.join(os.getcwd(), "requirements.txt"), "w").close()
    open(os.path.join(os.getcwd(), ".env"), "w").close()
