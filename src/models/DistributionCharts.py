import numpy as np
from vega_datasets import data

from src.models.base import ChartBase
import altair as alt
import pandas as pd


class HistogramHeatMap(ChartBase):
    def __init__(self):
        super().__init__(data.movies.url)
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).mark_rect().encode(
            alt.X('IMDB_Rating:Q').bin(maxbins=60),
            alt.Y('Rotten_Tomatoes_Rating:Q').bin(maxbins=40),
            alt.Color('count():Q').scale(scheme='greenblue')
        )


class LayeredHistogram(ChartBase):
    def __init__(self):
        super().__init__(pd.DataFrame({
            'Trial A': np.random.normal(0, 0.8, 1000),
            'Trial B': np.random.normal(-2, 1, 1000),
            'Trial C': np.random.normal(3, 2, 1000)
        }))
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).transform_fold(
            ['Trial A', 'Trial B', 'Trial C'],
            as_=['Experiment', 'Measurement']
        ).mark_bar(
            opacity=0.3,
            binSpacing=0
        ).encode(
            alt.X('Measurement:Q').bin(maxbins=100),
            alt.Y('count()').stack(None),
            alt.Color('Experiment:N')
        )


class StripPlotWJitter(ChartBase):
    def __init__(self):
        super().__init__(data.movies.url)
        self.chart = self.defineChart()

    def defineChart(self):
        gaussian_jitter = alt.Chart(self.dataset, title='Normally distributed jitter').mark_circle(size=8).encode(
            y="Major_Genre:N",
            x="IMDB_Rating:Q",
            yOffset="jitter:Q",
            color=alt.Color('Major_Genre:N').legend(None)
        ).transform_calculate(
            # Generate Gaussian jitter with a Box-Muller transform
            jitter="sqrt(-2*log(random()))*cos(2*PI*random())"
        )

        uniform_jitter = gaussian_jitter.transform_calculate(
            # Generate uniform jitter
            jitter='random()'
        ).encode(
            alt.Y('Major_Genre:N').axis(None)
        ).properties(
            title='Uniformly distributed jitter'
        )

        return (gaussian_jitter | uniform_jitter).resolve_scale(yOffset='independent')
