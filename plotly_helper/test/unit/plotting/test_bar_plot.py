import pytest

from plotly_helper.plotting import BarChart
from plotly.offline import plot

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

        BarChart(data['x'], data['y'])()

    def test_line_colour(self, data):
        """
        Checks that the line color setting works correctly.
        :param data:
        :return:
        """
        chart = BarChart(data['x'], data['y']).line_colour(
            'black').line_width(1.5).title('other')
        chart = chart.fill_opacity(0.7).fill_colour('green')()

    def test_axis_titles(self, data):
        """
        Checks axis titles
        :param data:
        :return:
        """

        chart = BarChart(data['x'], data['y']).xaxis.title('TITLE')()
        plot(chart)
