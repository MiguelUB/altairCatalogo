from vega_datasets import data
import altair as alt


class ChartBase:
    dataset = data.cars()
    chart = None

    def __init__(self, dataset):
        self.dataset = dataset


    def toJson(self, name):
        if self.chart is None:
            print('The chart has not been created yet')
        else:
            self.chart.save(name + '.json')

    def toHtml(self, name):
        if self.chart is None:
            print('The chart has not been created yet')
        else:
            self.chart.save(name + '.html')

    def defineChart(self):
        """
        This method will be inherited and every child will alter it
        """
        pass

    def setThemeChart(self):
        """
        This will change the colors and shapes of the chart when comparing
        :return:
        """
        pass