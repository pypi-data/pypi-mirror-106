import threading

from uncle_ben.logging import logger
from uncle_ben.basemodel import BaseModel


class EmptyModel(BaseModel):
    pass


class AnalyserException(Exception):
    pass


class BaseAnalyser(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(BaseAnalyser, self).__init__(*args, **kwargs)
        self._result = None
        self.ignored = "venv/*"

    @property
    def result(self):
        if not self._result:
            raise AnalyserException("Result not calculated yet!")
        return self._result

    def run(self):
        try:
            self._result = self.consolidate()
        except Exception as e:
            logger.error(e)
            self._result = EmptyModel()

    def consolidate(self):
        raise NotImplementedError()
