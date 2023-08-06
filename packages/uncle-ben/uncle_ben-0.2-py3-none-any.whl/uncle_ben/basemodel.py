import re
import enum

from pydantic import BaseModel as PydanticBaseModel


def _camel_case(string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()


class BaseModel(PydanticBaseModel):
    def dict(self, *args, **kwargs):
        _dict = super(BaseModel, self).dict()
        response = {}
        for key, value in _dict.items():
            name = self.__class__.__name__.replace("Consolidation", "")
            name = _camel_case(name)
            if isinstance(value, enum.Enum):
                response[name + "_" + _camel_case(key)] = value.value
            else:
                response[name + "_" + _camel_case(key)] = value
        return response
