"""Command-line entry point."""

import argparse
import json
from pathlib import Path

from .cleaner import clean_file
from .diagnostics import system_report


def main(argv: list[str] | None = None) -> int:
    """Run diagnostics or clean commands and return a process exit code."""
    parser = argparse.ArgumentParser(description="Agent workflow toolkit")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("diagnostics", help="report Git, Python, and Node versions")
    clean = commands.add_parser("clean", help="validate and normalize JSON records")
    clean.add_argument("source", type=Path)
    clean.add_argument("destination", type=Path)
    args = parser.parse_args(argv)
    if args.command == "diagnostics":
        print(json.dumps(system_report(), indent=2, sort_keys=True))
        return 0
    try:
        errors = clean_file(args.source, args.destination)
    except ValueError as error:
        parser.error(str(error))
    for error in errors:
        print(error)
    return 2 if errors else 0
