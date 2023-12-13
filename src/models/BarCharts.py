from altair import Chart
from ub_accesible_theme_altair.theme import accesible_theme
from ub_accesible_theme_altair.themes import tema_daltonimo_deuteranopia, black_theme
from ub_accesible_theme_altair.tokens import COLORS
from ub_accesible_theme_altair.utils import create_accesible_scheme

from vega_datasets import data
from ub_accesible_theme_altair import theme
import altair as alt

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
        super().__init__(data.wheat())
        self.chart = self.defineChart()

    def defineChart(self):
        base = alt.Chart(self.dataset).encode(
            x='wheat',
            y="year:O",
            text='wheat'
        )
        return base.mark_bar() + base.mark_text(align='left', dx=2)


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

