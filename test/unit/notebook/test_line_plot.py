import numpy as np
import pytest
from plotly.graph_objs import Scatter
from plotly.offline import plot

from plotting.line_plot import LinePlot

"""
Unit tests for the Lineplot class
"""


@pytest.fixture(scope="module")
def data():
    """
    Pytest fixture containing data to plot.
    :return:
    """
    x = np.arange(0, 10, 1)
    y = np.linspace(1, 2, 10)
    yield {'x': x, 'y': y}


@pytest.mark.usefixtures("data")
class TestLinePlot:

    def test_constructor(self, data):
        """
        Checks that the constructor API is correct.
        :return:
        """

        # Constructor should always take 2 arguments at minimum.
        LinePlot(data['x'], data['y'])

    def test_default_plot(self, data):
        """
        Check's that default plot has all the necessary components returned.
        :return:
        """
        plt = LinePlot(data['x'], data['y'])()

        assert len(plt['data']) == 1
        assert isinstance(plt['data'][0], Scatter)

    def test_colour_definition(self, data):
        """
        Checks that the colour method correctly modifies object and raises
        the right exceptions.
        :return:
        """

        plt = LinePlot(data['x'], data['y']).colour("maroon")()

        plot(plt)  # FIXME: Complete this test.

    def test_lines_style_definition(self, data):
        """
        Checks that line style is correctly applied.
        :param data:
        :return:
        """

        LinePlot(data['x'], data['y']).line_style('dot')()

    def test_axis_title(self, data):
        """
        Checks that the title correctly returns self.
        :param data:
        :return:
        """
        plot(LinePlot(data['x'], data['y']).title(None)())

    def test_add_plots(self, data):
        """
        Tests that the add operator works correctly.
        :param data:
        :return:
        """
        p1 = LinePlot(data['x'], data['y']).line_style('dot')
        p2 = LinePlot(data['x'],
                      data['y'] + np.random.randint(0, 3)).line_style('dot')

        p3 = (p1 + p2).title("Combined plot.")
        plot(p3())
