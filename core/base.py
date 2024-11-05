import argparse
import os
from importlib import import_module
from .utils.logging import logging, log_with_color, Fore


class BaseCommand:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="CLI tool to create scalable and modular Django projects."
        )
        self.subparsers = self.parser.add_subparsers(dest="command", help="Commands")

    def execute(self):
        """Parse and run user command"""
        args = self.parser.parse_args()
        args.base_dir = os.path.join(os.getcwd(), "src")

        if not args.command:
            self.parser.print_help()
            return

        if args.command == "help":
            try:
                help_module = import_module("commands.help")
                help_module.help()
            except ModuleNotFoundError:
                log_with_color(
                    logging.INFO,
                    "\nHelp command module not found.",
                    Fore.YELLOW,
                    delay=1,
                )
            return

        try:
            command_module = import_module(f"commands.{args.command}")
            log_with_color(logging.INFO, "Running commands...", Fore.BLUE, delay=2)
            command_module.run(args)
        except ModuleNotFoundError:
            log_with_color(
                logging.INFO,
                f"\nCommand {args.command} not found.",
                Fore.YELLOW,
                delay=1,
            )
            self.parser.print_help()

    def add_command(self, name, help_message, arguments=None):
        """Register a new subcommand"""
        command_parser = self.subparsers.add_parser(name, help=help_message)

        if arguments:
            for arg_name, arg_options in arguments.items():
                command_parser.add_argument(arg_name, **arg_options)


def main():
    cli = BaseCommand()
    cli.add_command(
        "project",
        "Create a new project.",
        arguments={
            "--api": {
                "help": "Include API setup",
                "action": "store_true",
            }
        },
    )
    cli.add_command("help", "Show help for a command.")
    cli.execute()
