from vega_datasets import data

from src.models.base import ChartBase
import altair as alt
import pandas as pd


class BumpChart(ChartBase):
    def __init__(self):
        stocks = data.stocks().groupby([pd.Grouper(key="date", freq="6M"), "symbol"]).mean().reset_index()
        super().__init__(stocks)
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).mark_line(point=True).encode(
            x=alt.X("date:O").timeUnit("yearmonth").title("date"),
            y="rank:O",
            color=alt.Color("symbol:N")
        ).transform_window(
            rank="rank()",
            sort=[alt.SortField("price", order="descending")],
            groupby=["date"]
        ).properties(
            title="Bump Chart for Stock Prices",
            width=600,
            height=150,
        )





class FilledStepChart(ChartBase):
    def __init__(self):
        super().__init__(data.stocks())
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).mark_area(
            color="lightblue",
            interpolate='step-after',
            line=True
        ).encode(
            x='date',
            y='price'
        ).transform_filter(alt.datum.symbol == 'GOOG')


class LineChartInterpolation(ChartBase):
    def __init__(self):
        super().__init__(data.sotcks())
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).mark_line(interpolate="monotone").encode(
            x="date:T",
            y="price:Q",
            color="symbol:N"
        )


class LineChartInterpolationWStrokes(ChartBase):
    def __init__(self):
        super().__init__(data.stocks())
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).mark_line(
            point=alt.OverlayMarkDef(filled=False, fill="white")
        ).encode(
            x='date:T',
            y='price:Q',
            color='symbol:N'
        )
