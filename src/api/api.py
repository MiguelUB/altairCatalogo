import json

import altair
from flask import Blueprint, request

from src.models.AreaCharts import *
from src.models.CircularPlots import *
from src.models.BarCharts import *
from src.models.DistributionCharts import *
from src.models.LineCharts import *
from src.models.MapsChart import *
from src.models.ScatterPlots import *
from src.models.TablesCharts import *

api_bp = Blueprint(
    "api_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/api",
)


@api_bp.route("/barchart", methods=["GET"])
def get_bar_chart():
    """
    This function will get a bar chart and return it in a json format
    Returns:
        Results (dict): Bar chart in vega configuration
    """
    base = None

    type_chart = request.args.get("type_chart").lower()
    theme_chart = request.args.get("theme_chart", "default").lower()

    if type_chart is None:
        return {"error": "type chart must be a type of bar chart like, bar_chart"}
    if theme_chart not in altair.themes.names():
        return {"error": "theme not registered in altair" + str(altair.themes.names())}

    if type_chart == "1":
        base = BarChart()
        base.setThemeChart(theme_chart)
    elif type_chart == "2":
        base = BarCharWLabels()
        base.setThemeChart(theme_chart)
    elif type_chart == "3":
        base = BarChartWRollingMean()
        base.setThemeChart(theme_chart)
    elif type_chart == "4":
        base = DivergingStackedBarChart()
        base.setThemeChart(theme_chart)

    return base.toJson()


@api_bp.route("/linechart", methods=["GET"])
def get_line_chart():
    """
    This function will get a bar chart and return it in a json format
    Returns:
        Results (dict): Bar chart in vega configuration
    """
    base = None

    type_chart = request.args.get("type_chart").lower()
    theme_chart = request.args.get("theme_chart", "default").lower()

    if type_chart is None:
        return {"error": "type chart must be a type of bar chart like, bar_chart"}
    if theme_chart not in altair.themes.names():
        return {"error": "theme not registered in altair" + str(altair.themes.names())}

    if type_chart == "1":
        base = BumpChart()
        base.setThemeChart(theme_chart)
    elif type_chart == "2":
        base = FilledStepChart()
        base.setThemeChart(theme_chart)
    elif type_chart == "3":
        base = LineChartInterpolation()
        base.setThemeChart(theme_chart)
    elif type_chart == "4":
        base = LineChartInterpolationWStrokes()
        base.setThemeChart(theme_chart)

    return base.toJson()
@api_bp.route("/areachart", methods=["GET"])
def get_area_charts():
    """
    This function will get a bar chart and return it in a json format
    Returns:
        Results (dict): Bar chart in vega configuration
    """
    base = None

    type_chart = request.args.get("type_chart").lower()
    theme_chart = request.args.get("theme_chart", "default").lower()

    if type_chart is None:
        return {"error": "type chart must be a type of bar chart like, bar_chart"}
    if theme_chart not in altair.themes.names():
        return {"error": "theme not registered in altair" + str(altair.themes.names())}

    if type_chart == "1":
        base = FacetedArea()
        base.setThemeChart(theme_chart)
    elif type_chart == "2":
        base = LayeredArea()
        base.setThemeChart(theme_chart)
    elif type_chart == "3":
        base = StreamGraph()
        base.setThemeChart(theme_chart)
    elif type_chart == "4":
        base = NormalizedStackedArea()
        base.setThemeChart(theme_chart)

    return base.toJson()
@api_bp.route("/circularplots", methods=["GET"])
def get_circular_plots():
    """
    This function will get a bar chart and return it in a json format
    Returns:
        Results (dict): Bar chart in vega configuration
    """
    base = None

    type_chart = request.args.get("type_chart").lower()
    theme_chart = request.args.get("theme_chart", "default").lower()

    if type_chart is None:
        return {"error": "type chart must be a type of bar chart like, bar_chart"}
    if theme_chart not in altair.themes.names():
        return {"error": "theme not registered in altair" + str(altair.themes.names())}

    if type_chart == "1":
        base = DonutChart()
        base.setThemeChart(theme_chart)
    elif type_chart == "2":
        base = PieChart()
        base.setThemeChart(theme_chart)
    elif type_chart == "3":
        base = RadialChart()
        base.setThemeChart(theme_chart)
    elif type_chart == "4":
        base = RadialChart()
        base.setThemeChart(theme_chart)

    return base.toJson()
@api_bp.route("/scatterplots", methods=["GET"])
def get_scatter_plots():
    """
    This function will get a bar chart and return it in a json format
    Returns:
        Results (dict): Bar chart in vega configuration
    """
    base = None

    type_chart = request.args.get("type_chart").lower()
    theme_chart = request.args.get("theme_chart", "default").lower()

    if type_chart is None:
        return {"error": "type chart must be a type of bar chart like, bar_chart"}
    if theme_chart not in altair.themes.names():
        return {"error": "theme not registered in altair" + str(altair.themes.names())}

    if type_chart == "1":
        base = ScatterWDataTable()
        base.setThemeChart(theme_chart)
    elif type_chart == "2":
        base = MultifeatureScatterPlot()
        base.setThemeChart(theme_chart)
    elif type_chart == "3":
        base = ScatterWHref()
        base.setThemeChart(theme_chart)
    elif type_chart == "4":
        base = ScatterWRollingMean()
        base.setThemeChart(theme_chart)

    return base.toJson()
@api_bp.route("/distributioncharts", methods=["GET"])
def get_distribution_charts():
    """
    This function will get a bar chart and return it in a json format
    Returns:
        Results (dict): Bar chart in vega configuration
    """
    base = None

    type_chart = request.args.get("type_chart").lower()
    theme_chart = request.args.get("theme_chart", "default").lower()

    if type_chart is None:
        return {"error": "type chart must be a type of bar chart like, bar_chart"}
    if theme_chart not in altair.themes.names():
        return {"error": "theme not registered in altair" + str(altair.themes.names())}

    if type_chart == "1":
        base = HistogramHeatMap()
        base.setThemeChart(theme_chart)
    elif type_chart == "2":
        base = LayeredHistogram()
        base.setThemeChart(theme_chart)
    elif type_chart == "3":
        base = StripPlotWJitter()
        base.setThemeChart(theme_chart)
    elif type_chart == "4":
        base = HistogramHeatMap()
        base.setThemeChart(theme_chart)

    return base.toJson()

@api_bp.route("/mapscharts", methods=["GET"])
def get_maps_charts():
    """
    This function will get a bar chart and return it in a json format
    Returns:
        Results (dict): Bar chart in vega configuration
    """
    base = None

    type_chart = request.args.get("type_chart").lower()
    theme_chart = request.args.get("theme_chart", "default").lower()

    if type_chart is None:
        return {"error": "type chart must be a type of bar chart like, bar_chart"}
    if theme_chart not in altair.themes.names():
        return {"error": "theme not registered in altair" + str(altair.themes.names())}

    if type_chart == "1":
        base = ChoroplethMap()
        base.setThemeChart(theme_chart)
    elif type_chart == "2":
        base = WindVectorMap()
        base.setThemeChart(theme_chart)
    elif type_chart == "3":
        base = PointMap()
        base.setThemeChart(theme_chart)
    elif type_chart == "4":
        base = WorldMap()
        base.setThemeChart(theme_chart)

    return base.toJson()

@api_bp.route("/tablescharts", methods=["GET"])
def get_tables_charts():
    """
    This function will get a bar chart and return it in a json format
    Returns:
        Results (dict): Bar chart in vega configuration
    """
    base = None

    type_chart = request.args.get("type_chart").lower()
    theme_chart = request.args.get("theme_chart", "default").lower()

    if type_chart is None:
        return {"error": "type chart must be a type of bar chart like, bar_chart"}
    if theme_chart not in altair.themes.names():
        return {"error": "theme not registered in altair" + str(altair.themes.names())}

    if type_chart == "1":
        base = AnnualWeatherHeatMap()
        base.setThemeChart(theme_chart)
    elif type_chart == "2":
        base = TextOverHeatmap()
        base.setThemeChart(theme_chart)
    elif type_chart == "3":
        base = AnnualWeatherHeatMap()
        base.setThemeChart(theme_chart)
    elif type_chart == "4":
        base = TextOverHeatmap()
        base.setThemeChart(theme_chart)

    return base.toJson()
