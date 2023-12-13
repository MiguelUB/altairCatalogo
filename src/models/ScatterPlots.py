from vega_datasets import data

from src.models.base import ChartBase
import altair as alt
import pandas as pd


class ScatterWDataTable(ChartBase):
    def __init__(self):
        self.chart = self.defineChart()

    def defineChart(self):
        # Brush for selection
        brush = alt.selection_interval()

        # Scatter Plot
        points = alt.Chart(self.dataset).mark_point().encode(
            x='Horsepower:Q',
            y='Miles_per_Gallon:Q',
            color=alt.condition(brush, alt.value('steelblue'), alt.value('grey'))
        ).add_params(brush)

        # Base chart for data tables
        ranked_text = alt.Chart(self.dataset).mark_text(align='right').encode(
            y=alt.Y('row_number:O').axis(None)
        ).transform_filter(
            brush
        ).transform_window(
            row_number='row_number()'
        ).transform_filter(
            alt.datum.row_number < 15
        )

        # Data Tables
        horsepower = ranked_text.encode(text='Horsepower:N').properties(
            title=alt.Title(text='Horsepower', align='right')
        )
        mpg = ranked_text.encode(text='Miles_per_Gallon:N').properties(
            title=alt.Title(text='MPG', align='right')
        )
        origin = ranked_text.encode(text='Origin:N').properties(
            title=alt.Title(text='Origin', align='right')
        )
        text = alt.hconcat(horsepower, mpg, origin)  # Combine data tables

        # Build chart
        return alt.hconcat(
            points,
            text
        ).resolve_legend(
            color="independent"
        ).configure_view(
            stroke=None
        )


class MultifeatureScatterPlot(ChartBase):
    def __init__(self):
        super().__init__(data.iris())
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).mark_circle().encode(
            alt.X('sepalLength').scale(zero=False),
            alt.Y('sepalWidth').scale(zero=False, padding=1),
            color='species',
            size='petalWidth'
        )


class ScatterWHref(ChartBase):
    def __init__(self):
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).transform_calculate(
            url='https://www.google.com/search?q=' + alt.datum.Name
        ).mark_point().encode(
            x='Horsepower:Q',
            y='Miles_per_Gallon:Q',
            color='Origin:N',
            href='url:N',
            tooltip=['Name:N', 'url:N']
        )


class ScatterWRollingMean(ChartBase):
    def __init__(self):
        super().__init__(data.seattle_weather())
        self.chart = self.defineChart()

    def defineChart(self):
        line = alt.Chart(self.dataset).mark_line(
            color='red',
            size=3
        ).transform_window(
            rolling_mean='mean(temp_max)',
            frame=[-15, 15]
        ).encode(
            x='date:T',
            y='rolling_mean:Q'
        )

        points = alt.Chart(self.dataset).mark_point().encode(
            x='date:T',
            y=alt.Y('temp_max:Q').title('Max Temp')
        )

        return points + line


class ScatterWtext(ChartBase):
    def __init__(self):
        super().__init__(pd.DataFrame({
            'x': [1, 3, 5, 7, 9],
            'y': [1, 3, 5, 7, 9],
            'label': ['A', 'B', 'C', 'D', 'E']
        })
        )
        self.chart = self.defineChart()

    def defineChart(self):
        points = alt.Chart(source).mark_point().encode(
            x='x:Q',
            y='y:Q'
        )

        text = points.mark_text(
            align='left',
            baseline='middle',
            dx=7
        ).encode(
            text='label'
        )

        return points + text
