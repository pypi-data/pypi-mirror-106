from uncle_ben.basemodel import BaseModel

from uncle_ben.analysers.radon.common import Radon


class RawMetrics(BaseModel):
    loc: int
    lloc: int
    sloc: int
    comments: int
    multi: int
    blank: int
    single_comments: int

    def __add__(self, other: 'RawMetrics'):
        return RawMetrics(
            loc=self.loc + other.loc,
            lloc=self.lloc + other.lloc,
            sloc=self.sloc + other.sloc,
            comments=self.comments + other.comments,
            multi=self.multi + other.multi,
            blank=self.blank + other.blank,
            single_comments=self.single_comments + other.single_comments
        )

    @classmethod
    def empty(cls):
        return RawMetrics(
            loc=0,
            lloc=0,
            sloc=0,
            comments=0,
            multi=0,
            blank=0,
            single_comments=0,
        )


class RawAnalyser(Radon):
    option = "raw"

    def consolidate(self) -> RawMetrics:
        entries = []
        for entry in self.output.values():
            entries.append(RawMetrics(**entry))
        if entries:
            return sum(entries[1:], start=entries[0])
        return RawMetrics.empty()
