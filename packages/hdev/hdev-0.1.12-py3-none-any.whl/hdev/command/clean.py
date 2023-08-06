"""Sub-command of `hdev` to clean projects."""
import os
import subprocess

import importlib_resources

from hdev.command.sub_command import SubCommand
from hdev.configuration import load_configuration


class Clean(SubCommand):
    """Sub-command of `hdev` to print out python version information."""

    name = "clean"
    help = "Clean a project directory"

    DEFAULT_CLEAN = {
        "files": ["node_modules/.uptodate", ".coverage"],
        "dirs": [
            "build",
            "build.eggs",
            "dist",
            "*.egg-info",
            "src/*.egg-info",
            ".coverage.*",
            ".pytest_cache",
        ],
        "file_names": ["*.py[co]"],
        "dir_names": ["__pycache__"],
        "empty_dirs": True,
    }
    DEEP_CLEAN = {"dirs": [".tox", "node_modules"]}

    @classmethod
    def configure_parser(cls, parser):
        """Set up arguments needed for the sub-command."""
        parser.add_argument(
            "--all",
            "-a",
            action="store_true",
            help="Clean everything we know how to clean.",
        )

        parser.add_argument(
            "--deep",
            "-d",
            action="store_true",
            help="Clean items which might be slow to rebuild like tox and node modules",
        )

        parser.add_argument(
            "--branches",
            "-b",
            action="store_true",
            help="Clean and prune old and detached git branches as well",
        )

    def __call__(self, args):
        """Run the command.

        :param args: An ArgParser Namespace object
        """
        os.chdir(args.project_dir)

        # Merge any project specific settings with our defaults
        config = load_configuration(args.project_file).get("tool.hdev.clean", {})
        to_clean = dict(self.DEFAULT_CLEAN)
        for key in to_clean:
            if isinstance(to_clean[key], list):
                to_clean[key].extend(config.get(key, []))
            else:
                to_clean[key] = config.get(key, to_clean[key])

        self._clean(**to_clean, verbose=args.debug)

        if args.deep or args.all:
            self._clean(**self.DEEP_CLEAN, verbose=args.debug)

        if args.branches or args.all:
            self._run_script("clean_branches.sh")

    @classmethod
    def _clean(
        # pylint: disable=too-many-arguments
        cls,
        files=None,
        dirs=None,
        file_names=None,
        dir_names=None,
        verbose=False,
        empty_dirs=False,
    ):
        script_lines = []
        for options, items in (("--force", files), ("--recursive --force", dirs)):
            if verbose:
                options += " --verbose"
            if items:
                script_lines.append(f"rm {options} {' '.join(items)}")

        if file_names:
            name_selector = " -or ".join([f'-name "{item}"' for item in file_names])

            script_lines.append(f"find . -type f \\( {name_selector} \\) -delete")

        if empty_dirs or dir_names:
            selectors = []
            if empty_dirs:
                selectors.append("-empty")

            if dir_names:
                selectors.extend([f'-name "{item}"' for item in dir_names])

            dir_selector = " -or ".join(selectors)

            rm_command = "rm --recursive"
            if verbose:
                rm_command += " --verbose"

            script_lines.append(
                f"find . -type d \\( {dir_selector} \\) -exec {rm_command} {{}} +"
            )

        script_content = ";".join(script_lines)

        subprocess.check_call(script_content, shell=True)

    _BIN_DIR = importlib_resources.files("hdev.resources.bin")

    @classmethod
    def _run_script(cls, script_name):
        with importlib_resources.as_file(cls._BIN_DIR / script_name) as script:
            subprocess.check_call([str(script)])
