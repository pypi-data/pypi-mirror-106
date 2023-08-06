import enum
import typing


class Rank(enum.Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"

    @classmethod
    def average_rank(cls, ranks: typing.List['Rank']):
        if not ranks:
            return cls.A
        translate = {cls.A: 5, cls.B: 4, cls.C: 3,
                     cls.D: 2, cls.E: 1, cls.F: 0}
        value = sum([translate[r] for r in ranks])
        average = round(value / len(ranks))
        average_index = list(translate.values()).index(average)
        return cls(list(translate.keys())[average_index])
