from math import log2

from uncle_ben.analysers.radon.common import Radon
from uncle_ben.basemodel import BaseModel


class Halstead(BaseModel):
    n1: int
    n2: int
    N1: int
    N2: int
    vocabulary: int
    length: int
    calculated_length: float
    volume: float
    difficulty: float
    effort: float
    time: float
    bugs: float

    @classmethod
    def empty(cls):
        return cls.from_list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0])

    @classmethod
    def from_list(cls, argument_list):
        return cls(**dict(zip(Halstead.__fields__.keys(),
                              argument_list)))


class HalsteadAnalyser(Radon):
    option = "hal"

    def consolidate(self) -> Halstead:
        entries = []
        for entry in self.output.values():
            entries.append(Halstead.from_list(entry["total"]))
        """Program vocabulary: n = n1 + n2
           Program length: N = N1 + N2
           Calculated program length: N'=n1log2(n1)+n2log2(n2)
           Volume: V= Nlog2(n)
           Difficulty: D= (n1/2) * (N2/n2)
           Effort: E= DV
           Time required to program: T= E/18 seconds
           Number of delivered bugs: B=V/3000
        """

        if entries:
            n1 = sum([e.n1 for e in entries])
            n2 = sum([e.n2 for e in entries])
            N1 = sum([e.N1 for e in entries])
            N2 = sum([e.N2 for e in entries])
            vocabulary = n1 + n2
            length = N1 + N2
            calculated_length = sum([e.calculated_length
                                     for e in entries]) / len(entries)
            volume = length * log2(vocabulary)
            difficulty = (n1 / 2) * (N2 / n2)
            effort = difficulty * volume
            time = effort / 18
            bugs = volume / 3000
            return Halstead(
                n1=n1,
                n2=n2,
                N1=N1,
                N2=N2,
                vocabulary=vocabulary,
                length=length,
                calculated_length=calculated_length,
                volume=volume,
                difficulty=difficulty,
                effort=effort,
                time=time,
                bugs=bugs
            )
        return Halstead.empty()
