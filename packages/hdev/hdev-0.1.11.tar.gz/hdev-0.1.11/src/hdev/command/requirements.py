"""Sub-command of `hdev` to manipulate requirements files."""
import sys

from hdev.command.sub_command import SubCommand
from hdev.requirements import RequirementsFile, compile_unpinned


class Requirements(SubCommand):
    """Sub-command of `hdev` to manipulate requirements files."""

    name = "requirements"
    help = "Compiles .txt requirements file based on the existing .in files using pip-tools"

    @classmethod
    def configure_parser(cls, parser):
        """Set up arguments needed for the sub-command."""

        parser.add_argument(
            "--package",
            required="--file" in sys.argv,
            dest="package",
            help="Upgrade a single package or set it to a specific version. "
            "Use `package-name` for the latest, or `package-name=1.2.3` "
            "for a specific version",
        )

        parser.add_argument(
            "--file",
            dest="upgrade_targets",
            nargs="+",
            help="If --package is specified, limit upgrades to this specific "
            "requirements file. Can be specified multiple times",
        )

    def __call__(self, args):
        """Run the command.

        :param args: An ArgParser Namespace object
        """
        unpinned_files = RequirementsFile.find(args.project_dir / "requirements/")

        # Compile the files
        compiled = list(
            self._compile(
                unpinned_files=unpinned_files,
                upgrade_targets=self._upgrade_targets(args, unpinned_files),
                package=args.package,
            )
        )

        # Report back
        if not compiled:
            print("No requirements files found.")
            return

        print("Compiled:")
        for unpinned_file, pinned_file in compiled:
            print(f"\t{unpinned_file} >> {pinned_file}")

    @classmethod
    def _compile(cls, unpinned_files, upgrade_targets, package):
        for unpinned_file in unpinned_files:
            specific_package = package if unpinned_file in upgrade_targets else None

            print(f"Compiling {unpinned_file} (package={specific_package})")
            try:
                pinned_file = compile_unpinned(
                    unpinned_file=unpinned_file,
                    specific_package=specific_package,
                )
            except FileNotFoundError:
                print("\t... file not found")
                continue

            yield [unpinned_file, pinned_file]

    @classmethod
    def _upgrade_targets(cls, args, unpinned_files):
        if args.package and args.upgrade_targets:
            upgrade_targets = {
                RequirementsFile(path).absolute() for path in args.upgrade_targets
            }

            missing = upgrade_targets - set(unpinned_files)
            if missing:
                raise ValueError(
                    f"Specified files '{missing}' not in the list of "
                    "files to be processed"
                )

            return upgrade_targets

        return set(unpinned_files)
