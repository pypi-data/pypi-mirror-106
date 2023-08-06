import pathlib
import re
import typing

import pydantic

from uncle_ben.analysers.base import BaseAnalyser
from uncle_ben.command import cmd


class PackageUsageFormat(pydantic.BaseModel):
    packages: typing.List[str]
    count: int
    packages_installed: typing.List[str]

    @classmethod
    def empty(cls):
        return cls(packages=[], count=0, installed=[])


class PackageUsage(pydantic.BaseModel):
    setup_packages: typing.List[str]
    setup_count: int
    setup_installed: typing.List[str]
    requirements_packages: typing.List[str]
    requirements_count: int
    requirements_installed: typing.List[str]


# TODO: implement package usage
# https://pypi.org/project/pip-package-list/


class PackageUsageAnalyser(BaseAnalyser):
    @staticmethod
    def analyse_file(filename) -> PackageUsageFormat:
        path = pathlib.Path(filename)
        if not path.exists():
            return PackageUsageFormat.empty()

        pip_compile_output = cmd(f"pip-compile --dry-run {filename}")
        pip_compile_output = re.sub("#.*\n", "", pip_compile_output)

        def filter_line(line):
            return line.replace(" ", "").split("=")[0]

        # remove last line "Dry-run, so nothing updated."
        packages_installed = list(map(filter_line,
                                      pip_compile_output.split("\n")[:-1]))

        pip_list = cmd(f"pip-package-list {filename}").split("\n")
        return PackageUsageFormat(packages=pip_list,
                                  count=len(pip_list),
                                  packages_installed=packages_installed)

    def consolidate(self):
        setup = self.analyse_file('setup.py')
        requirements = self.analyse_file("requirements.txt")
        return PackageUsage(
            setup_packages=setup.packages,
            setup_count=setup.count,
            setup_installed=setup.packages_installed,
            requirements_packages=requirements.packages,
            requirements_count=requirements.count,
            requirements_installed=requirements.packages_installed,
        )


if __name__ == '__main__':
    pua = PackageUsageAnalyser()
    pua.consolidate()
