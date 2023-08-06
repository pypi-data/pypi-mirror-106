# TODO parse
# Metrics: presence and number of steps,
# maybe some keyword for each step (lint, build, test ?)
import os

from uncle_ben.basemodel import BaseModel
from uncle_ben.analysers.base import BaseAnalyser


class GitlabCI(BaseModel):
    present: bool


class GitlabCIAnalyser(BaseAnalyser):
    def consolidate(self):
        present = os.path.exists(".gitlab-ci.yml")

        return GitlabCI(
            present=present
        )

    # TODO: parse .gitlab-ci.yml
    # Metrics: presence and number of steps,
    # maybe some keyword for each step (lint, build, test ?)
