from vega_datasets import data

from src.models.base import ChartBase
import altair as alt
import pandas as pd


class AnnualWeatherHeatMap(ChartBase):
    def __init__(self):
        super().__init__(data.seattle_weather())
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset, title="Daily Max Temperatures (C) in Seattle, WA").mark_rect().encode(
            alt.X("date(date):O").title("Day").axis(format="%e", labelAngle=0),
            alt.Y("month(date):O").title("Month"),
            alt.Color("max(temp_max)").title(None),
            tooltip=[
                alt.Tooltip("monthdate(date)", title="Date"),
                alt.Tooltip("max(temp_max)", title="Max Temp"),
            ],
        ).configure_view(
            step=13,
            strokeWidth=0
        ).configure_axis(
            domain=False
        )


class TextOverHeatmap(ChartBase):
    def __init__(self):
        super().__init__(data.cars())
        self.chart = self.defineChart()

    def defineChart(self):
        base = alt.Chart(self.dataset).transform_aggregate(
            mean_horsepower='mean(Horsepower)',
            groupby=['Origin', 'Cylinders']
        ).encode(
            alt.X('Cylinders:O'),
            alt.Y('Origin:O'),
        )

        # Configure heatmap
        heatmap = base.mark_rect().encode(
            alt.Color('mean_horsepower:Q')
            .scale(scheme='viridis')
            .title("Mean of Horsepower")
        )

        # Configure text
        text = base.mark_text(baseline='middle').encode(
            alt.Text('mean_horsepower:Q', format=".0f"),
            color=alt.condition(
                alt.datum.mean_horsepower > 150,
                alt.value('black'),
                alt.value('white')
            )
        )

        # Draw the chart
        return heatmap + text


