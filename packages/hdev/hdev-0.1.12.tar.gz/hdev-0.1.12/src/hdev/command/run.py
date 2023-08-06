from subprocess import check_call

from hdev.command.sub_command import SubCommand
from hdev.configuration import load_configuration


class Run(SubCommand):
    """Sub-command of `hdev` to run custom commands."""

    name = "run"
    help = "Run a custom command defined in the pyproject.toml file"

    @classmethod
    def configure_parser(cls, parser):
        """Set up arguments needed for the sub-command."""

        parser.add_argument("command", nargs=1, help="Custom command to run")

    def __call__(self, args):
        """Run the command.

        :param args: An ArgParser Namespace object
        :raises FileNotFoundError: If no project file is found
        """
        if not args.project_file.exists():
            raise FileNotFoundError(
                f"Cannot find command configuration in '{args.project_file}'. "
                f"Try changing directory to the project first."
            )

        config = load_configuration(args.project_file).get("tool.hdev.run", {})

        self._run_command(config, command_name=args.command[0], debug=args.debug)

    @classmethod
    def _run_command(cls, config, command_name, debug=False):
        command_details = config.get(command_name)
        if not command_details:
            raise ValueError(
                f"No such command found: '{command_name}'. "
                f"Did you mean one of: {list(config.keys())}"
            )

        shell_command = command_details.get("command")
        if not shell_command:
            raise ValueError(f"Expected to find key 'command' in: {command_details}")

        if debug:
            print(f"Running: {shell_command}")

        check_call(shell_command, shell=True)
