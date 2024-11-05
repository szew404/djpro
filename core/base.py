import argparse
import sys
from importlib import import_module


class BaseCommand:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="CLI tool to create scalable and modular Django projects."
        )
        self.subparsers = self.parser.add_subparsers(
            dest="command", help="Available commands"
        )

    def execute(self):
        """Parse and run user command"""
        args = self.parser.parse_args()
        if not args.command:
            self.parser.print_help()
            sys.exit(1)

        try:
            command_module = import_module(f"django_cli_tool.commands.{args.command}")
            command_module.run(args)
        except ModuleNotFoundError:
            print(f"Comando '{args.command}' no encontrado.")
            self.parser.print_help()

    def add_command(self, name, help_message):
        """Register a new subcommand"""
        self.subparsers.add_parser(name, help=help_message)


def main():
    cli = BaseCommand()
    cli.add_command("create_project", "Create a new project.")
    cli.add_command("help", "Show help")
    cli.execute()
