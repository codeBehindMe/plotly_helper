from abc import ABCMeta, abstractmethod

"""Contains abstract classes for implementation"""


# FIXME: Docstrings in this module need to be done.

class Chart(metaclass=ABCMeta):

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class XAxis:
    def __init__(self, caller):
        self.caller = caller

    def title(self, value):
        self.caller.layout['xaxis'] = value
        return self.caller


class Yaxis:
    def __init__(self, caller):
        self.caller = caller

    def title(self, value):
        self.caller.layout['yaxis'] = value
        return self.caller
