import sys

from lib.constants.build_platforms import build_platforms
from lib.services.build_strategies import build_strategies
from lib.exceptions.DirNotFound import DirNotFoundException

def builder(build_platform=build_platforms['REACT_NATIVE']):
    class Builder():

        def __init__(self):
            self.build_platform = build_platform

        def build(self):
            try:
                build_strategies()[self.build_platform]()
            except DirNotFoundException as e:
                print(e.message)
                sys.exit(1)

    return Builder
