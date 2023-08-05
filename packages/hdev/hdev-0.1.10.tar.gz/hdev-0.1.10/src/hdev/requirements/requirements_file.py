"""hdev requirements implementation."""
import os
from functools import cached_property
from glob import glob
from pathlib import PosixPath

from pkg_resources import resource_filename

from hdev.requirements.parse import parse

PIP_TOOLS_REQS = resource_filename("hdev", "resources/requirements/pip-tools.txt")


class RequirementsFile(PosixPath):
    """Represents a pinned, or unpinned requirements file."""

    @property
    def tox_env(self):
        """Get the tox env used with this file."""
        return "dev" if self.stem == "requirements" else self.stem

    @property
    def tox_env_requirements_file(self):
        """Get the requirements file used in the tox env for this file."""
        return RequirementsFile(self.with_name(f"{self.tox_env}.txt"))

    @property
    def pinned_file(self):
        """Get the pinned version of this file."""

        return RequirementsFile(self.with_suffix(".txt").absolute())

    @property
    def unpinned_file(self):
        """Get the unpinned version of this file."""

        return RequirementsFile(self.with_suffix(".in").absolute())

    @property
    def file_references(self):
        """Get any references from this file to other requirements files.

        :returns: A list of RequirementsFile objects
        """

        return (req for req in self._requirements if isinstance(req, RequirementsFile))

    @cached_property
    def _requirements(self):
        return list(
            parse(
                lines=self.read_text("utf-8").split("\n"),
                base_dir=self.parent,
                ref_factory=lambda op, filename: RequirementsFile(filename)
                if op == "-r"
                else None,
            )
        )

    @classmethod
    def find(cls, requirements_dir):
        """Find unpinned requirements in a directory.

        :return: An iterable of RequirementsFile in an order that is safe to
            compile
        """
        req_files = {}

        for file_name in glob(os.path.join(requirements_dir, "*.in")):
            req_file = cls(file_name).unpinned_file
            req_files[req_file] = [
                ref.unpinned_file for ref in req_file.file_references
            ]

        # Generate a sort key which is always bigger than any parents we
        # depend on
        def sort_key(req_file):
            return 1 + sum(sort_key(parent) for parent in req_files[req_file])

        return sorted(req_files, key=sort_key)
