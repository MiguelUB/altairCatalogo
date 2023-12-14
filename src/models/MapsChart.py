from vega_datasets import data

from src.models.base import ChartBase
import altair as alt
import pandas as pd


class ChoroplethMap(ChartBase):
    def __init__(self):
        super().__init__(alt.topo_feature(data.us_10m.url, 'counties'), data.unemployment.url)
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.Chart(self.dataset).mark_geoshape().encode(
            color='rate:Q'
        ).transform_lookup(
            lookup='id',
            from_=alt.LookupData(self.dataset2, 'id', ['rate'])
        ).project(
            type='albersUsa'
        ).properties(
            width=500,
            height=300
        )


class WindVectorMap(ChartBase):
    def __init__(self):
        super().__init__(data.windvectors(), alt.topo_feature(data.world_110m.url, "countries"))
        self.chart = self.defineChart()

    def defineChart(self):
        wedge = alt.Chart(self.dataset).mark_point(shape="wedge", filled=True).encode(
            alt.Latitude("latitude"),
            alt.Longitude("longitude"),
            alt.Color("dir")
            .scale(domain=[0, 360], scheme="rainbow")
            .legend(None),
            alt.Angle("dir").scale(domain=[0, 360], range=[180, 540]),
            alt.Size("speed").scale(rangeMax=500)
        ).project("equalEarth")

        xmin, xmax, ymin, ymax = (
            self.dataset.longitude.min(),
            self.dataset.longitude.max(),
            self.dataset.latitude.min(),
            self.dataset.latitude.max(),
        )

        # extent as feature or featurecollection
        extent = {
            "type": "Feature",
            "geometry": {"type": "Polygon",
                         "coordinates": [[
                             [xmax, ymax],
                             [xmax, ymin],
                             [xmin, ymin],
                             [xmin, ymax],
                             [xmax, ymax]]]
                         },
            "properties": {}
        }

        # use fit combined with clip=True
        base = (
            alt.Chart(self.dataset2)
            .mark_geoshape(clip=True, fill="lightgray", stroke="black", strokeWidth=0.5)
            .project(type="equalEarth", fit=extent)
        )

        return base + wedge


class PointMap(ChartBase):
    def __init__(self):
        super().__init__(data.airports.url, alt.topo_feature(data.us_10m.url, feature='states'))
        self.chart = self.defineChart()

    def defineChart(self):
        background = alt.Chart(self.dataset2).mark_geoshape(
            fill='lightgray',
            stroke='white'
        ).properties(
            width=500,
            height=300
        ).project('albersUsa')

        # Airports grouped by state
        points = alt.Chart(self.dataset, title='Number of airports in US').transform_aggregate(
            latitude='mean(latitude)',
            longitude='mean(longitude)',
            count='count()',
            groupby=['state']
        ).mark_circle().encode(
            longitude='longitude:Q',
            latitude='latitude:Q',
            size=alt.Size('count:Q').title('Number of Airports'),
            color=alt.value('steelblue'),
            tooltip=['state:N', 'count:Q']
        )

        return background + points


class WorldMap(ChartBase):
    sphere = alt.sphere()
    graticule = alt.graticule()

    def __init__(self):
        super().__init__(alt.topo_feature(data.world_110m.url, 'countries'))
        self.chart = self.defineChart()

    def defineChart(self):
        return alt.layer(
            alt.Chart(self.sphere).mark_geoshape(fill='lightblue'),
            alt.Chart(self.graticule).mark_geoshape(stroke='white', strokeWidth=0.5),
            alt.Chart(self.dataset).mark_geoshape(fill='ForestGreen', stroke='black')
        ).project(
            'naturalEarth1'
        ).properties(width=600, height=400).configure_view(stroke=None)



