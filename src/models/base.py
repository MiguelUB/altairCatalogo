import json

from vega_datasets import data
import altair as alt


class ChartBase:
    dataset = data.cars()
    chart = None

    def __init__(self, dataset):
        self.dataset = dataset


    def toJson(self):
        return json.loads(self.chart.to_json())



    def defineChart(self):
        """
        This method will be inherited and every child will alter it
        """
        pass

    def setThemeChart(self,name_theme):
        """
        This will change the colors and shapes of the chart when comparing
        :return:
        """
        alt.themes.enable(name_theme)
        self.chart = self.defineChart()
