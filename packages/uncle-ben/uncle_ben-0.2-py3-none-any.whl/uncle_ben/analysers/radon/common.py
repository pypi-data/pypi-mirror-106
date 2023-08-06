import json

from uncle_ben.command import cmd
from uncle_ben.analysers.base import BaseAnalyser


class Radon(BaseAnalyser):
    option = "-h"

    def __init__(self):
        super(Radon, self).__init__()
        self._output = None

    @property
    def output(self):
        if not self._output:
            self.get_output()
        return self._output

    def get_output(self):
        command = f"radon {self.option} -j ."
        if self.ignored:
            command += " -i {self.ignored}"
        out = cmd(command)
        self._output = json.loads(out[:out.rfind("}")+1])
        return self._output
