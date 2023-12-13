import json

import altair
from flask import Blueprint, request

from src.models.BarCharts import BarChart, BarCharWLabels, StackedBarChar
from src.models.base import ChartBase

api_bp = Blueprint(
    "api_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/api",
)


@api_bp.route("/barchart", methods=["GET"])
def get_chart():
    """
    This function will get a bar chart and return it in a json format
    Returns:
        Results (dict): Bar chart in vega configuration
    """
    base = None

    type_chart = request.args.get("type_chart").lower()
    theme_chart = request.args.get("theme_chart", "default").lower()
    print("FFFFF", request.args, type(type_chart), theme_chart)

    if type_chart is None:
        return {"error": "type chart must be a type of bar chart like, bar_chart"}
    if theme_chart not in altair.themes.names():
        return {"error": "theme not registered in altair" + str(altair.themes.names())}

    if type_chart == "1":
        base = BarChart()
        base.setThemeChart(theme_chart)
    elif type_chart == "2":
        base = BarCharWLabels()
    elif type_chart == "3":
        base = StackedBarChar()
    print(base)

    return base.toJson()
