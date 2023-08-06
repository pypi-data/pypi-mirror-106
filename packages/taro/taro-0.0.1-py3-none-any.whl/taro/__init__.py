
import yaml
import json
from pathlib import Path

from . import util
from . import exceptions


class Pipeline:

    @classmethod
    def fromJSON(cls, filename):
        pass

    @classmethod
    def fromYAML(cls, filename):
        pass

    def __init__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        return str(self)

    def toJSON(self, filename):
        pass

    def toYAML(self, filename):
        pass


class Stage:
    def __init__(self):
        pass

