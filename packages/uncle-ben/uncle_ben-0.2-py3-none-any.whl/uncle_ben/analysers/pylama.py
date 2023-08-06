import re

from uncle_ben.analysers.base import BaseAnalyser
from uncle_ben.basemodel import BaseModel
from uncle_ben.command import cmd


class PyLama(BaseModel):
    pycodestyle: int
    pydocstyle: int
    pyflakes: int
    mccabe: int
    pylint: int
    pep8: int
    pep257: int


class PyLamaAnalyser(BaseAnalyser):
    OUTPUT_PARSER = re.compile(
        r"([-.\w/_ ]*:\d*:\d*):[ \t]*([-_ ,\'\"\w\d#]*) *\[(\w*)\]"
    )

    @classmethod
    def find_outputs(cls, output):
        return cls.OUTPUT_PARSER.findall(output)

    def consolidate(self):
        command = "pylama"
        if self.ignored:
            command += f" -i {self.ignored}"
        result = {
            "pycodestyle": 0,
            "pydocstyle": 0,
            "pyflakes": 0,
            "mccabe": 0,
            "pylint": 0,
            "pep8": 0,
            "pep257": 0,
        }
        entries = []
        for linter in result.keys():
            linter_output = cmd(f"{command} -s {linter}")
            entries.extend(self.find_outputs(linter_output))

        for file, error, linter in entries:
            result[linter] += 1
        return PyLama(**result)
