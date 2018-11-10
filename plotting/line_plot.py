import plotly.graph_objs as go

from abstraction.meta import Chart
from abstraction.meta import XAxis
from abstraction.meta import Yaxis


class LinePlot(Chart):
    def __add__(self, other):
        pass

    def __call__(self, *args, **kwargs):
        self._compile_scatter_object()
        return dict(data=self.data, layout=self.layout)

    def __init__(self, x, y, **kwargs):
        """
        Instantiates a line plot.

        Line plots are implemented as Scatter graph objects.
        :param x: X coordinates. of line.
        :param y: Y coordinates of line.
        :param kwargs: Additional arguments for formatting the line.
        """
        self.x = x
        self.y = y
        self.layout = {}
        self.data = []
        self.line = {}

        self.name = kwargs.get("name", None)

        self.dot = kwargs.get("linestyle", None)

        self.title = kwargs.get("title", None)

    def title(self, value):
        """
        Adds a title to the plot.
        :param value: Title value
        :return:
        """
        self.layout['title'] = value

    def colour(self, value):
        """
        Sets the colour of the line
        :param value: Colour
        :return:
        """
        # FIXME: Implement the colour system.
        raise NotImplementedError()

    def line_width(self, value):
        """
        Set the line width.
        :param value:
        :return:
        """
        self.line['width'] = value

    def line_style(self, value):
        """
        Set's the line style.
        :param value:
        :return:
        """
        # FIXME: Implement the line style system.
        raise NotImplementedError()

    @property
    def xaxis(self):
        """
        Defining the x-axis parameters.
        :return:
        """
        return XAxis(self)

    @property
    def yaxis(self):
        """
        Defining the y-axis parameters.
        :return:
        """
        return Yaxis(self)

    def _compile_scatter_object(self):
        """
        Compiles a plotly scatter object and assigns it to the data list.
        :return:
        """
        self.data.append(go.Scatter(x=self.x, y=self.y, name=self.name))
