from vega_datasets import data
import altair as alt
import pandas as pd
from src.models.base import ChartBase


class BarChart(ChartBase):
    def __init__(self):
        super().__init__(data.wheat())
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).mark_bar().encode(
            x='year:O',
            y="wheat:Q",
            # The highlight will be set on the result of a conditional statement
        )


class BarCharWLabels(ChartBase):
    def __init__(self):
        super().__init__(data.barley())
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).mark_bar().encode(
            x='variety',
            y='sum(yield)',
            color='site'
        )


class StackedBarChar(ChartBase):
    def __init__(self):
        super().__init__(data.barley())
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).mark_bar().encode(
            x='variety',
            y='sum(yield)',
            color='site'
        )


class BarChartWRollingMean(ChartBase):
    def __init__(self):
        super().__init__(data.wheat())
        self.chart = self.defineChart()

    def defineChart(self):
        bar = alt.Chart(self.dataset).mark_bar().encode(
            x='year:O',
            y='wheat:Q'
        )

        line = alt.Chart(self.dataset).mark_line(color='red').transform_window(
            # The field to average
            rolling_mean='mean(wheat)',
            # The number of values before and after the current value to include.
            frame=[-9, 0]
        ).encode(
            x='year:O',
            y='rolling_mean:Q'
        )

        return (bar + line).properties(width=600)


class DivergingStackedBarChart(ChartBase):
    source = pd.DataFrame(
        [
            {"a": "a1", "b": "b1", "c": "x", "p": "0.14"},
            {"a": "a1", "b": "b1", "c": "y", "p": "0.60"},
            {"a": "a1", "b": "b1", "c": "z", "p": "0.03"},
            {"a": "a1", "b": "b2", "c": "x", "p": "0.80"},
            {"a": "a1", "b": "b2", "c": "y", "p": "0.38"},
            {"a": "a1", "b": "b2", "c": "z", "p": "0.55"},
            {"a": "a1", "b": "b3", "c": "x", "p": "0.11"},
            {"a": "a1", "b": "b3", "c": "y", "p": "0.58"},
            {"a": "a1", "b": "b3", "c": "z", "p": "0.79"},
            {"a": "a2", "b": "b1", "c": "x", "p": "0.83"},
            {"a": "a2", "b": "b1", "c": "y", "p": "0.87"},
            {"a": "a2", "b": "b1", "c": "z", "p": "0.67"},
            {"a": "a2", "b": "b2", "c": "x", "p": "0.97"},
            {"a": "a2", "b": "b2", "c": "y", "p": "0.84"},
            {"a": "a2", "b": "b2", "c": "z", "p": "0.90"},
            {"a": "a2", "b": "b3", "c": "x", "p": "0.74"},
            {"a": "a2", "b": "b3", "c": "y", "p": "0.64"},
            {"a": "a2", "b": "b3", "c": "z", "p": "0.19"},
            {"a": "a3", "b": "b1", "c": "x", "p": "0.57"},
            {"a": "a3", "b": "b1", "c": "y", "p": "0.35"},
            {"a": "a3", "b": "b1", "c": "z", "p": "0.49"},
            {"a": "a3", "b": "b2", "c": "x", "p": "0.91"},
            {"a": "a3", "b": "b2", "c": "y", "p": "0.38"},
            {"a": "a3", "b": "b2", "c": "z", "p": "0.91"},
            {"a": "a3", "b": "b3", "c": "x", "p": "0.99"},
            {"a": "a3", "b": "b3", "c": "y", "p": "0.80"},
            {"a": "a3", "b": "b3", "c": "z", "p": "0.37"},
        ]
    )

    def __init__(self):
        super().__init__(self.source)
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset, width=60, height=alt.Step(8)).mark_bar().encode(
            alt.Y("c:N").axis(None),
            alt.X("p:Q").title(None).axis(format="%"),
            alt.Color("c:N").title("settings").legend(orient="bottom", titleOrient="left"),
            alt.Row("a:N").title("Factor A").header(labelAngle=0),
            alt.Column("b:N").title("Factor B"),
        )




