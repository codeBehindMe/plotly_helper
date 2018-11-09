import numpy as np
import pytest

from notebook.line_plot import LinePlot

"""
Unit tests for the Lineplot class
"""


@pytest.fixture(scope="module")
def data():
    """
    Pytest fixture containing data to plot.
    :return:
    """
    x = np.arange(0, 1, 10)
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

        assert len(plt['data']) > 0
