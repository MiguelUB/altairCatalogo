import json

from vega_datasets import data
import altair as alt


class ChartBase:
    dataset = data.cars()
    dataset2 = data.wheat()
    chart = None

    def __init__(self, dataset, dataset2=data.wheat()):
        self.dataset = dataset
        self.dataset2 = dataset2

    def toJson(self):
        """
        This function use the altair function to_json() wich returns a dict and
        with the dict we send return a JSON format
        :return: A JSON with all the information to render in vega-lite the graph
        """
        return json.loads(self.chart.to_json())

    def defineChart(self):
        """
        This method will be inherited and every child will alter it
        """
        pass

    def setThemeChart(self, name_theme):
        """
        This function will re-define the chart now using the theme given
        """
        alt.themes.enable(name_theme)
        self.chart = self.defineChart()
