import pytest
from plotly.offline import plot

from plotting.bar_chart import BarChart

"""
Unit test for the BarPlot class
"""


@pytest.fixture(scope="module")
def data():
    """
    Data for plotting.
    :return:
    """

    x = ['First', 'Second', 'Third']
    y = [35, 45, 25]
    yield {'x': x, 'y': y}


@pytest.mark.usefixtures("data")
class TestBarPlot:

    def test_constructor(self, data):
        """
        Checks that the constructor works correctly.
        :param data:
        :return:
        """

        chart = BarChart(data['x'], data['y'])()
        # plot(chart)

    def test_line_colour(self,data):
        """
        Checks that the line color setting works correctly.
        :param data:
        :return:
        """
        chart = BarChart(data['x'], data['y']).line_colour('black').line_width(1.5)
        chart = chart.fill_opacity(0.7).fill_colour('green')()

        plot(chart)
