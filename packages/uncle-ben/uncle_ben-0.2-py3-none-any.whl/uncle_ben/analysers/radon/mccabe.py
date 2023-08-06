import typing
from statistics import mean, stdev

from uncle_ben.analysers.radon.common import Radon
from uncle_ben.analysers.radon.rank import Rank
from uncle_ben.basemodel import BaseModel


class McCabeFormat(BaseModel):
    rank: Rank
    type: str
    col_offset: typing.Optional[int]
    lineno: typing.Optional[int]
    complexity: int
    name: str
    endline: typing.Optional[int]
    closures: typing.Optional[typing.List]


class McCabe(BaseModel):
    rank: Rank
    total_complexity: int
    max_complexity: int
    mean_complexity: float
    stddev_complexity: float


class McCabeAnalyser(Radon):
    option = "cc"

    def consolidate(self) -> McCabe:
        entries = []
        for file_entries in self.output.values():
            for entry in file_entries:
                # TODO: this consolidation should take closures into account
                entries.append(McCabeFormat(**entry))
        rank = Rank.average_rank([e.rank for e in entries])
        total_complexity = sum([e.complexity for e in entries])
        max_complexity = max([e.complexity for e in entries])
        mean_complexity = mean([e.complexity for e in entries])
        stddev_complexity = stdev([e.complexity for e in entries])
        return McCabe(rank=rank,
                      max_complexity=max_complexity,
                      mean_complexity=mean_complexity,
                      stddev_complexity=stddev_complexity,
                      total_complexity=total_complexity)
