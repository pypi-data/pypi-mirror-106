from datetime import datetime

from dateutil import parser

from uncle_ben.analysers.base import BaseAnalyser
from uncle_ben.basemodel import BaseModel
from uncle_ben.command import cmd

GIT_LOG = "git log --no-merges --format=\"%ae|%cd\""
GIT_LOG_MERGES = "git log --merges --format=\"%ae|%cd\""


class Git(BaseModel):
    number_of_committers: int
    number_of_commits: int
    first_commit: datetime
    last_commit: datetime
    number_merges: int


class GitAnalyser(BaseAnalyser):
    def __init__(self):
        super().__init__()
        self._commits = None
        self._merges = None
        self._dates = None
        self._committers = None

    @property
    def commits(self):
        if not self._commits:
            self._commits = [line.split("|")
                             for line in cmd(GIT_LOG).split("\n")]
        return self._commits

    @property
    def merges(self):
        if not self._merges:
            self._merges = [line.split("|")
                            for line in cmd(GIT_LOG_MERGES).split("\n")]
        return self._merges

    @property
    def dates(self):
        if not self._dates:
            self._dates = set([parser.parse(gl[1]) for gl in self.commits])
        return self._dates

    @property
    def committers(self):
        if not self._committers:
            self._committers = set([gl[0] for gl in self.commits])
        return self._committers

    def number_of_committers(self):
        return len(self.committers)

    def number_of_commits(self):
        return len(self.commits)

    def number_of_merges(self):
        return len(self.merges)

    def first_commit(self):
        return min(self.dates)

    def last_commit(self):
        return max(self.dates)

    def consolidate(self) -> Git:
        return Git(
            number_of_committers=self.number_of_committers(),
            number_of_commits=self.number_of_commits(),
            first_commit=self.first_commit(),
            last_commit=self.last_commit(),
            number_merges=self.number_of_merges()
        )
