import os
import pathlib
import re
from tempfile import TemporaryDirectory
from enum import Enum

from uncle_ben.analysers import analysers
from uncle_ben.command import cmd


class TargetType(Enum):
    DIRECTORY = 0
    GIT = 0


class Directory:
    def __init__(self, target):
        self.target = target

    def enter(self):
        os.chdir(self.target)


class GitDirectory:
    def __init__(self, target):
        self.url = target
        self._tmpdir = TemporaryDirectory()

    def __del__(self):
        del self._tmpdir

    def clone(self):
        cmd(f"git clone {self.url} {self._tmpdir.name}")

    def enter(self):
        self.clone()
        os.chdir(self._tmpdir.name)


def is_git_url(target: str):
    """

    https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols

    https://example.com/gitproject.git
    https://user@example.com/gitproject.git
    ssh://user@server/project.git
    ssh://server/project.git
    git@github.com:user/project.git
    github.com:user/project.git
    :return:
    """
    if not target.endswith(".git"):
        return False
    matching_git_with_prefix = r'(\w+://)(.+@)*([\w\d\.]+)(:[\d]+){0,1}/*(.*)'
    match = re.match(matching_git_with_prefix, target)
    if match and match.string == target:
        return True
    matching_git_without_prefix = r'(.+@)*([\w\d\.]+)(:[\d]+){0,1}/*(.*)'
    match = re.match(matching_git_without_prefix, target)
    if match and match.string == target:
        return True
    return False


class Repository:
    def __init__(self, target: str):
        self.target = target
        self.handler = self.determine_target_type(target)

    def enter(self):
        self.handler.enter()

    @staticmethod
    def determine_target_type(target):
        if pathlib.Path(target).exists():
            return Directory(target)
        elif is_git_url(target):
            return GitDirectory(target)

    def complete_analysis(self):
        self.enter()
        analysers_list = [analyser() for analyser in analysers]
        for analyser in analysers_list:
            analyser.start()
        for analyser in analysers_list:
            analyser.join()
        result = {}
        for analyser in analysers_list:
            result.update(analyser.result.dict())
        return result
