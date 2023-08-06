"""Entry point for the hdev script."""
import pathlib
import sys
from argparse import ArgumentParser

from hdev import command


class HParser(ArgumentParser):
    """Overwrites ArgumentParser to control the `error` behaviour."""

    def error(self, message):
        """Change the default behavior to print help on errors."""
        sys.stderr.write("error: %s\n" % message)
        self.print_help()
        sys.exit(2)


def create_parser():
    """Create the root parser for the `hdev` command."""

    parser = HParser()

    parser.add_argument(
        "--project-dir",
        type=pathlib.Path,
        default=pathlib.Path("."),
        help="Path of the project's root. Defaults to .",
    )

    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debugging info",
    )

    subparsers = parser.add_subparsers()

    for sub_command in [
        command.Alembic(),
        command.Clean(),
        command.Deps(),
        command.PythonVersion(),
        command.Requirements(),
        command.Run(),
        command.Template(),
    ]:
        sub_command.add_to_parser(subparsers)

    return parser


def hdev():
    """Create an argsparse cmdline tools to expose hdev functionality.

    Main entry point of hdev
    """
    parser = create_parser()
    args = parser.parse_args()

    # When we are using Python 3.7, this can be replaced with
    # add_argument(required=True) above
    try:
        handler = getattr(args, "handler")
    except AttributeError:
        parser.print_help()
        sys.exit(2)

    args.project_file = args.project_dir / "pyproject.toml"
    args.tox_file = args.project_dir / "tox.ini"

    try:
        handler(args)

    except SystemExit:  # pylint: disable=try-except-raise
        # The handler is controlling the exit, and we should respect that
        raise

    except Exception as err:  # pylint: disable=broad-except
        if args.debug:
            raise

        # Another error has been raised, so dump it and print the help too
        print(f"Error: {err}\n")
        parser.print_usage()
        sys.exit(2)


if __name__ == "__main__":  # pragma: nocover
    hdev()
