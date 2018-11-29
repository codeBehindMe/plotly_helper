from setuptools import setup

setup(name='plotly_helper', version='0.1',
    packages=['plotly_helper', 'plotly_helper.test',
              'plotly_helper.test.unit', 'plotly_helper.test.unit.plotting',
              'plotly_helper.service', 'plotly_helper.plotting',
              'plotly_helper.abstraction'],
    url='https://github.com/codeBehindMe/plotly_helper', license='MIT',
    author='Machine  Sciences Lab',
    author_email='aaron.tillekeratne@gmail.com',
    description='Quick helper for plotly.')
