import json

from flask import Blueprint, render_template

from src.models.BarCharts import BarChart
import altair as alt
import pandas as pd

charts_bp = Blueprint(
    "charts_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@charts_bp.route("/barcharts", methods=["GET"])
def bar_charts_view():
    base = BarChart()
    base.setThemeChart("dark")

    return render_template(
        "bar_charts_view.html",
        title="Bar Charts",
        chartData=base.toJson()
    )


@charts_bp.route("/linecharts", methods=["GET"])
def line_charts_view():
    return render_template(
        "line_charts_view.html",
        title="Pomodoretis"
    )


@charts_bp.route("/areacharts", methods=["GET"])
def area_charts_view():
    return render_template(
        "area_charts_view.html",
        title="Pomodoretis"
    )


@charts_bp.route("/circularplots", methods=["GET"])
def circular_plots_view():
    return render_template(
        "circular_plots_view.html",
        title="Pomodoretis"
    )


@charts_bp.route("/scatterplots", methods=["GET"])
def scatter_plots_view():
    return render_template(
        "scatter_plots_view.html",
        title="Pomodoretis"
    )


@charts_bp.route("/distribution", methods=["GET"])
def distribution_view():
    return render_template(
        "distribution_view.html",
        title="Pomodoretis"
    )


@charts_bp.route("/maps", methods=["GET"])
def maps_view():
    return render_template(
        "maps_view.html",
        title="Pomodoretis"
    )


@charts_bp.route("/tables", methods=["GET"])
def tables_view():
    return render_template(
        "tables_view.html",
        title="Pomodoretis"
    )
