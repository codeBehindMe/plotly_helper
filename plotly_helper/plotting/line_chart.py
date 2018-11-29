from copy import deepcopy

import plotly.graph_objs as go


from plotly_helper.abstraction.constants import COLOUR_RGB_MAP
from plotly_helper.abstraction.constants import LINE_STYLE_MAP
from plotly_helper.abstraction.meta import Chart
from plotly_helper.abstraction.meta import XAxis
from plotly_helper.abstraction.meta import YAxis


class LineChart(Chart):

    def __add__(self, other):
        """
        Adds another plot to this chart. This isn't multiplot , this is just
        adding two lines or overlaying plots together.

        Currently this only supports other line charts.
        :param other: Other chart.
        :return:
        """

        # Make a new plot with this object as a copy.
        new_plot = deepcopy(self)
        # Append the other scatter object to the new plot.
        new_plot.data.append(other.get_plotly_object())

        # Combine layouts
        new_plot.layout = {**other.layout, **self.layout}

        return new_plot

    def __call__(self, *args, **kwargs):
        self._prepare_plot_package()
        return dict(data=self.data, layout=go.Layout(**self.layout))

    def __init__(self, x, y, **kwargs):
        """
        Instantiates a line plot.

        Line plots are implemented as Scatter graph objects.
        :param x: X coordinates. of line.
        :param y: Y coordinates of line.
        :param kwargs: Additional arguments for formatting the line.
        """
        super().__init__()
        self.x = x
        self.y = y
        self.line = {}
        self.line_name = None

        # Assign properties if given.
        self.name(kwargs.get("name", None))
        self.title(kwargs.get("title", None))
        self.colour(kwargs.get("colour", None))

    def name(self, value):
        """
        Line name
        :param value:
        :return:
        """
        self.line_name = value
        return self

    def title(self, value):
        """
        Adds a title to the plot.
        :param value: Title value
        :return:
        """
        self.layout['title'] = value
        return self

    def colour(self, value):
        """
        Sets the colour of the line
        :param value: Colour
        :return:
        """
        if value is None:
            self.line['color'] = None
            return self
        try:
            self.line['color'] = COLOUR_RGB_MAP[value.lower()]
            return self
        except KeyError:
            raise KeyError(
                "Invalid colour definition. Please select from {0}".format(
                    COLOUR_RGB_MAP.keys()))

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
        try:
            self.line['dash'] = LINE_STYLE_MAP[value.lower()]
            return self
        except KeyError:
            raise KeyError("Invalid line style definition. \
                Please select from {0}".format(LINE_STYLE_MAP.keys()))

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
        return YAxis(self)

    def get_plotly_object(self):
        """
        Return the scatter object without changing object state.
        :return:
        """
        return go.Scatter(x=self.x, y=self.y, name=self.line_name,
                          line=self.line)

    def _prepare_plot_package(self):
        """
        Compiles a plotly scatter object and assigns it to the data list.
        :return:
        """
        # Insert to front if there is already a scatter object from an add
        # operation. Since our scatter
        self.data.insert(0, self.get_plotly_object())
