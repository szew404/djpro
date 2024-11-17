# This file is part of djpro.
#
# Copyright (c) 2024, Franco Gidaszewski <gidaszewskifranco@gmail.com>
#
# For the full copyright and license information, please view
# the LICENSE.txt file that was distributed with this source code.

from pathlib import Path

from ..utils.logging import logging, log_with_color, Fore
from ..utils.messages import run_dev, run_prod
from ..utils.django_utils import generate_secret_key
from ..utils.write_and_config import (
    create_dirs,
    create_files,
    write_to_file,
    configure_requirements,
    configure_settings_base,
)
from ..utils.files_content import (
    settings_content,
    settings_dev_content,
    settings_prod_content,
    wsgi_content,
    asgi_content,
    urls_content,
    env_dev_content,
    requirements_content,
    gitignore_content,
    views_auth_content,
    urls_auth_content,
    manage_content,
    dockerfile_content,
    dockercompose_content,
    env_prod_content,
    env_prod_db_content,
    urls_api_content,
)


def create_project(
    base_dir: Path,
    project_name: str,
    api: bool = False,
    docker: bool = False,
    unfold: bool = False,
):
    """Function to create directories and files"""

    base_dir_path = Path(base_dir)

    # Directories
    directories = [
        base_dir_path / "bin",
        base_dir_path / "config",
        base_dir_path / "static",
        base_dir_path / "modules",
        base_dir_path / "modules" / "authentication",
        base_dir_path / "utils",
        base_dir_path / "tests",
        base_dir_path / "templates",
    ]

    # Files
    project_files = [
        base_dir_path / "bin" / "__init__.py",
        base_dir_path / "bin" / "manage.py",
        base_dir_path / "config" / "__init__.py",
        base_dir_path / "config" / "settings.py",
        base_dir_path / "config" / "settings_base.py",
        base_dir_path / "config" / "settings_prod.py",
        base_dir_path / "config" / "settings_dev.py",
        base_dir_path / "config" / "asgi.py",
        base_dir_path / "config" / "wsgi.py",
        base_dir_path / "config" / "urls.py",
        base_dir_path / "config" / ".env.conf",
        base_dir_path / "modules" / "__init__.py",
        base_dir_path / "modules" / "authentication" / "__init__.py",
        base_dir_path / "modules" / "authentication" / "serializers.py",
        base_dir_path / "modules" / "authentication" / "models.py",
        base_dir_path / "modules" / "authentication" / "views.py",
        base_dir_path / "modules" / "authentication" / "urls.py",
        base_dir_path / "utils" / "__init__.py",
        base_dir_path / "tests" / "__init__.py",
    ]

    root_files = [
        Path(".env.dev"),
        Path(".gitignore"),
        Path("requirements.txt"),
    ]

    if docker:
        log_with_color(
            logging.INFO,
            "\nConfiguring Docker...",
            Fore.WHITE,
            delay=2,
        )
        docker_files = [
            Path(".env.prod"),
            Path(".env.prod.db"),
            Path("Dockerfile"),
            Path("docker-compose.yml"),
        ]
        for file in docker_files:
            root_files.append(file)

    if api:
        log_with_color(
            logging.INFO,
            "\nConfiguring Django Rest Framework...",
            Fore.WHITE,
            delay=1,
        )

        api_dir = base_dir_path / "modules" / "api"
        directories.append(api_dir)

        api_files = [
            base_dir_path / "modules" / "api" / "__init__.py",
            base_dir_path / "modules" / "api" / "serializers.py",
            base_dir_path / "modules" / "api" / "models.py",
            base_dir_path / "modules" / "api" / "views.py",
            base_dir_path / "modules" / "api" / "urls.py",
        ]
        for file in api_files:
            project_files.append(file)

    log_with_color(logging.INFO, "Creating directories...", Fore.BLUE)
    create_dirs(directories)  # Create dirs

    log_with_color(logging.INFO, "Almost ready...", Fore.YELLOW, delay=3)
    create_files(project_files + root_files)  # Create files
    write(base_dir, project_name, api, docker, unfold)  # Write files


def write(
    base_dir: Path,
    project_name: str,
    api: bool = False,
    docker: bool = False,
    unfold: bool = False,
):
    """Function to write the content in each file of the project."""
    log_with_color(logging.INFO, "Configuring files...", Fore.YELLOW, delay=3)

    base_dir_path = Path(base_dir)
    config_dir = base_dir_path / "config"
    bin_dir = base_dir_path / "bin"
    auth_module_dir = base_dir_path / "modules" / "authentication"

    files_to_write = [
        (
            config_dir / ".env.conf",
            "DJANGO_ENV=dev",
        ),  # Development environment by default
        (
            config_dir / "settings.py",
            settings_content.format(project_name=project_name),
        ),
        (config_dir / "settings_dev.py", settings_dev_content),
        (config_dir / "settings_prod.py", settings_prod_content),
        (config_dir / "wsgi.py", wsgi_content.format(project_name=project_name)),
        (config_dir / "asgi.py", asgi_content.format(project_name=project_name)),
        (config_dir / "urls.py", urls_content.format(project_name=project_name)),
        (bin_dir / "manage.py", manage_content),
        (auth_module_dir / "views.py", views_auth_content),
        (auth_module_dir / "urls.py", urls_auth_content),
        (Path("requirements.txt"), requirements_content),
        (Path(".gitignore"), gitignore_content),
        (Path(".env.dev"), env_dev_content.format(secret_key=generate_secret_key())),
    ]

    if api:
        files_to_write[6] = (
            config_dir / "urls.py",
            urls_api_content.format(project_name=project_name),
        )

    if docker:
        # Set production environment
        files_to_write[0] = (
            config_dir / ".env.conf",
            "DJANGO_ENV=prod",
        )

        docker_files = [
            (
                Path(".env.prod"),
                env_prod_content.format(secret_key=generate_secret_key()),
            ),
            (Path(".env.prod.db"), env_prod_db_content),
            (Path("Dockerfile"), dockerfile_content),
            (Path("docker-compose.yml"), dockercompose_content),
        ]
        for file in docker_files:
            files_to_write.append(file)

    for file_path, content in files_to_write:
        write_to_file(file_path, content)

    # settings_base.py
    settings_base_content = configure_settings_base(api, unfold)
    write_to_file(config_dir / "settings_base.py", settings_base_content)

    # sub-commands requirements.txt
    additional_requirements = configure_requirements(api, unfold)
    if additional_requirements:
        write_to_file(Path("requirements.txt"), additional_requirements, mode="a")


def run(args):
    """Entry point for command 'project'."""

    try:
        create_project(
            base_dir=args.base_dir,
            project_name=args.project_name,
            api=args.api,
            docker=args.docker,
            unfold=args.unfold,
        )

        log_with_color(logging.INFO, "---- Project created successfully.", Fore.GREEN)

        log_with_color(
            logging.INFO,
            "\nIMPORTANT:\n",
            Fore.YELLOW,
        )

        # Messages
        if args.docker:
            run_prod.run_prod_messages()
        else:
            run_dev.run_dev_messages()

    except Exception as e:
        log_with_color(
            logging.INFO,
            f"\nError while creating project: {e}",
            Fore.RED,
        )
