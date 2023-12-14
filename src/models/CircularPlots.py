from src.models.base import ChartBase
import altair as alt
import pandas as pd


class DonutChart(ChartBase):
    def __init__(self):
        super().__init__(pd.DataFrame({
            "category": [1, 2, 3, 4, 5, 6],
            "value": [4, 6, 10, 3, 7, 8]
        })
        )
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).mark_arc(innerRadius=50).encode(
            theta="value",
            color="category:N",
        )


class PieChart(ChartBase):
    def __init__(self):
        super().__init__(pd.DataFrame({"category": [1, 2, 3, 4, 5, 6], "value": [4, 6, 10, 3, 7, 8]}))
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).mark_arc().encode(
            theta="value",
            color="category"
        )


class RadialChart(ChartBase):
    def __init__(self):
        super().__init__(pd.DataFrame({"values": [12, 23, 47, 6, 52, 19]}))
        self.chart = self.defineChart()

    def defineChart(self):
        base = alt.Chart(self.dataset).encode(
            alt.Theta("values:Q").stack(True),
            alt.Radius("values").scale(type="sqrt", zero=True, rangeMin=20),
            color="values:N",
        )

        c1 = base.mark_arc(innerRadius=20, stroke="#fff")

        c2 = base.mark_text(radiusOffset=10).encode(text="values:Q")

        return c1 + c2



