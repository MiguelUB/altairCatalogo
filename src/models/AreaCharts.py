from vega_datasets import data

from src.models.base import ChartBase
import altair as alt
import pandas as pd


class FacetedArea(ChartBase):
    def __init__(self):
        super().__init__(data.stocks())
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).transform_filter(alt.datum.symbol != "GOOG").mark_area().encode(
            x="date:T",
            y="price:Q",
            color="symbol:N",
            row=alt.Row("symbol:N").sort(["MSFT", "AAPL", "IBM", "AMZN"]),
        ).properties(height=50, width=400)


class LayeredArea(ChartBase):
    def __init__(self):
        super().__init__(data.iowa_electricity())
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).mark_area(opacity=0.3).encode(
            x="year:T",
            y=alt.Y("net_generation:Q").stack(None),
            color="source:N"
        )


class StreamGraph(ChartBase):
    def __init__(self):
        super().__init__(data.unemployment_across_industries.url)
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).mark_area().encode(
            alt.X('yearmonth(date):T').axis(format='%Y', domain=False, tickSize=0),
            alt.Y('sum(count):Q').stack('center').axis(None),
            alt.Color('series:N').scale(scheme='category20b')
        ).interactive()


class NormalizedStackedArea(ChartBase):
    def __init__(self):
        super().__init__(data.iowa_electricity())
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).mark_area().encode(
            x="year:T",
            y=alt.Y("net_generation:Q").stack("normalize"),
            color="source:N"
        )
