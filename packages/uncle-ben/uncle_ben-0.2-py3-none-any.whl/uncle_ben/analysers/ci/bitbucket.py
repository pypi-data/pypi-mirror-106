import os

from uncle_ben.basemodel import BaseModel
from uncle_ben.analysers.base import BaseAnalyser


class BitbucketCI(BaseModel):
    present: bool


class BitbucketCIAnalyser(BaseAnalyser):
    def consolidate(self):
        present = os.path.exists("bitbucket-pipelines.yml")

        return BitbucketCI(
            present=present
        )

    # TODO: parse bitbucket-pipelines.yml
    # Metrics: presence and number of steps,
    # maybe some keyword for each step (lint, build, test ?)
