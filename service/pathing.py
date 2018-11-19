import inspect
import os
import sys


def set_path():
    return sys.path.append(
        os.path.abspath(os.path.join('..', inspect.stack()[0])))
