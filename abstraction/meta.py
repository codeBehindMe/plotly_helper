from abc import ABCMeta, abstractmethod

"""Contains abstract classes for implementation"""


# FIXME: Docstrings in this module need to be done.

class Chart(metaclass=ABCMeta):

    def __init__(self):
        self.layout = {'xaxis': {}, 'yaxis': {}}
        self.data = []

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_plotly_object(self):
        """
        Returns the plotly object for the class.

        Example: Scatter(x,y...)
        :return:
        """
        pass

    @abstractmethod
    def _prepare_plot_package(self):
        """
        Prepares the class for the plot / iplot call from plotly.
        :return:
        """
        pass

    @property
    @abstractmethod
    def xaxis(self):
        pass

    @property
    @abstractmethod
    def yaxis(self):
        pass

    def title(self, value):
        """
        Set's the chart title.
        :param value:
        :return:
        """
        self.layout['title'] = value
        return self


class XAxis:
    def __init__(self, caller):
        self.caller = caller

    def title(self, value):
        self.caller.layout['xaxis']['title'] = value
        return self.caller

    def tickangle(self, value):
        self.caller.layout['xaxis']['tickangle'] = value
        return self.caller


class YAxis:
    def __init__(self, caller):
        self.caller = caller

    def title(self, value):
        self.caller.layout['yaxis']['title'] = value
        return self.caller

    def tickangle(self, value):
        self.caller.layout['yaxis']['tickangle'] = value
        return self.caller
