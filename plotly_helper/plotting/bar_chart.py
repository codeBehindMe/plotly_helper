import plotly.graph_objs as go

from plotly_helper.abstraction import COLOUR_RGB_MAP
from plotly_helper.abstraction import Chart
from plotly_helper.abstraction import YAxis
from plotly_helper.abstraction import XAxis


class BarChart(Chart):
    @property
    def xaxis(self):
        return XAxis(self)

    @property
    def yaxis(self):
        return YAxis(self)

    def __add__(self, other):
        pass

    def __call__(self, *args, **kwargs):
        self._prepare_plot_package()
        return dict(data=self.data, layout=go.Layout(**self.layout))

    def get_plotly_object(self):
        return go.Bar(x=self.x, y=self.y, name=self.bar_name,
                      opacity=self.opacity, marker=self.marker)

    def _prepare_plot_package(self):
        self.data.insert(0, self.get_plotly_object())

    def __init__(self, x, y, text=None, **kwargs):
        """
        # FIXME: Docstring
        :param x: Bar keys
        :param y: Bar values
        :param text: Text for each of the bars for hover.
        :param kwargs:  Other optionals
        """
        super().__init__()
        self.x = x
        self.y = y
        self.text = text
        self.marker = {'line': {}}

        self.bar_name = None
        self.bar_mode = None
        self.opacity = 1.0

        self.name(kwargs.get("name", None))

    def name(self, value):
        """
        Name of the bars.
        :param value:
        :return:
        """

        self.bar_name = value
        return self

    def fill_colour(self, value):
        """
        Bar fill colour.
        :param value:
        :return:
        """

        if value is None:
            return self
        try:
            self.marker['color'] = COLOUR_RGB_MAP[value.lower()]
            return self
        except KeyError:
            raise KeyError(
                "Invalid colour definition. Please select from {0}".format(
                    COLOUR_RGB_MAP.keys()))

    def line_colour(self, value):
        """
        Colour of the border.
        :param value:
        :return:
        """
        if value is None:
            return self
        try:
            self.marker['line']['color'] = COLOUR_RGB_MAP[value.lower()]
            return self
        except KeyError:
            raise KeyError(
                "Invalid colour definition. Please select from {0}".format(
                    COLOUR_RGB_MAP.keys()))

    def line_width(self, value):
        """
        Line width of the border.
        :param value:
        :return:
        """
        self.marker['line']['width'] = value
        return self

    def fill_opacity(self, value):
        """
        Fill opacity.
        :param value:
        :return:
        """
        self.opacity = value
        return self
