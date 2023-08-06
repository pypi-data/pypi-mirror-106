"""Sub-command of `hdev` to list dependencies."""
import sys
from subprocess import Popen

from jinja2 import Environment, PackageLoader

from hdev.command.sub_command import SubCommand
from hdev.model.project import Project
from hdev.requirements import OUR_LIBS
from hdev.requirements.graph import DependencyGraph
from hdev.requirements.package import Package
from hdev.requirements.tree import DependencyTree
from hdev.shell import Color

IGNORE_LIBS = {"setuptools", "six"}


class Deps(SubCommand):
    """Sub-command of `hdev` to list dependencies."""

    name = "deps"
    help = "Get dependency information"

    jinja_env = Environment(
        loader=PackageLoader("hdev", package_path="resources/templates")
    )

    @classmethod
    def configure_parser(cls, parser):
        """Set up arguments needed for the sub-command."""
        parser.add_argument("--package", "-p", help="Get details of a specific package")

        parser.add_argument(
            "--graph",
            "-g",
            action="store_true",
            help="Graph the dependencies",
        )

        parser.add_argument(
            "--python-version",
            default="3.9",
            help="Specify the target python version (for graphing)",
        )

        parser.add_argument(
            "--python-version-max",
            help="Specify the max python version (for graphing)",
        )

        parser.add_argument(
            "--show",
            "-s",
            action="store_true",
            help="Open the graph for viewing once made",
        )

        parser.add_argument(
            "--output-file",
            "-o",
            help="Specify a filename (for graphing)",
        )

        parser.add_argument(
            "--verbose",
            "-v",
            action="store_true",
            help="Dump additional data",
        )

    def __call__(self, args):
        """Run the command.

        :param args: An ArgParser Namespace object
        """

        target_package = None
        project = None

        if args.package:
            target_package = Package(args.package)
            requirements = {"install": target_package.requirements}

        else:
            project = Project(args.project_dir)
            requirements = project.requirements()

        print(
            self.jinja_env.get_template("dep_command.txt.jinja2")
            .render(
                target_package=target_package,
                project=project,
                requirements=requirements,
                verbose=args.verbose,
                color=Color,
                our_libs=OUR_LIBS,
            )
            .strip()
        )

        if args.graph:
            self._create_graph(args, requirements)

    @classmethod
    def _create_graph(cls, args, requirements):
        node_filter = None
        if not args.verbose:
            node_filter = DependencyTree.standard_node_filter(
                maximum_python_version=args.python_version_max or args.python_version,
                ignore_libs=IGNORE_LIBS,
                no_dependencies=OUR_LIBS,
            )

        dot = DependencyGraph.create_dot(
            tree=DependencyTree.create(requirements, node_filter=node_filter),
            target_python_version=args.python_version,
        )

        if args.debug:
            print("Graphviz dot ----------------------------")
            print(dot)
            print("End of graphviz dot ----------------------------")

        output_file = args.output_file
        if not args.output_file:
            if args.package:
                graph_name = args.package
            else:
                graph_name = args.project_dir.absolute().name

            output_file = f"{graph_name}_deps.png"

        DependencyGraph.create_png(dot=dot, output_file=output_file)
        if args.show:
            # Using Popen rather than check_output etc. means we don't attach
            # to stderr etc. and end up waiting for the sub-process to finish
            Popen(["open" if sys.platform == "darwin" else "xdg-open", output_file])

        print(f"Created: {output_file}")
