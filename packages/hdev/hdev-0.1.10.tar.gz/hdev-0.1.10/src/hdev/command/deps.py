"""Sub-command of `hdev` to list dependencies."""
from hdev.command.sub_command import SubCommand
from hdev.requirements.package import Package


class Deps(SubCommand):
    name = "deps"
    help = "Get dependency information"

    @classmethod
    def configure_parser(cls, parser):
        """Set up arguments needed for the sub-command."""
        parser.add_argument(
            "--package", "-p", required=True, help="Get details of a specific package"
        )

    def __call__(self, args):
        """Run the command.

        :param args: An ArgParser Namespace object
        """

        self._dump_package_details(Package(args.package), verbose=True)

    @classmethod
    def _dump_package_details(cls, package, verbose, indent=0):  # pragma: no cover
        latest_version, _ = package.latest_release
        version_string = f"(latest: {latest_version})"

        python_version = cls._python_version_string(package)

        indent = "\t" * indent

        print(
            f"{indent}{package.canonical_name: <20} {version_string: <18} Python {python_version}"
        )
        if verbose:
            for url_type, url in sorted(package.urls.items()):
                print(f"{indent}\t{url_type}: {url}")
            print()

    @classmethod
    def _python_version_string(cls, package):  # pragma: no cover
        if package.python_versions:
            latest_version = package.python_versions[-1]
        else:
            latest_version = "???"

        declared = package.declared_versions
        if declared:
            latest_declared = declared[-1]
        else:
            latest_declared = "???"

        if latest_version == latest_declared:
            return latest_declared

        return f"{latest_version} (declared: {latest_declared})"
