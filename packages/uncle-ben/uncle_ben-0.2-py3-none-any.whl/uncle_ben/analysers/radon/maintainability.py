from statistics import mean, stdev

from uncle_ben.analysers.radon.common import Radon
from uncle_ben.analysers.radon.rank import Rank
from uncle_ben.basemodel import BaseModel


class MaintainabilityFormat(BaseModel):
    rank: Rank
    mi: float


class Maintainability(BaseModel):
    rank: Rank
    total_maintainability: float
    max_maintainability: float
    mean_maintainability: float
    stddev_maintainability: float


class MaintainabilityAnalyser(Radon):
    option = "mi"

    def consolidate(self) -> Maintainability:
        entries = []
        for entry in self.output.values():
            # TODO: this consolidation should take closures into account
            entries.append(MaintainabilityFormat(**entry))
        if not entries:
            return Maintainability(rank=Rank.A,
                                   total_maintainability=0,
                                   max_maintainability=0,
                                   stddev_maintainability=0,
                                   mean_maintainability=0)

        rank = Rank.average_rank([e.rank for e in entries])
        total_maintainability = sum([e.mi for e in entries])
        max_maintainability = max([e.mi for e in entries])
        mean_maintainability = mean([e.mi for e in entries])
        stddev_maintainability = stdev([e.mi for e in entries])
        return Maintainability(
            rank=rank,
            total_maintainability=total_maintainability,
            max_maintainability=max_maintainability,
            stddev_maintainability=stddev_maintainability,
            mean_maintainability=mean_maintainability)
