import json

from flask import Blueprint, render_template, redirect

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

    return render_template(
        "bar_charts_view.html",
        title="Bar Charts",

    )


@charts_bp.route("/linecharts", methods=["GET"])
def line_charts_view():
    return render_template(
        "line_charts_view.html",
        title="Line Charts"
    )


@charts_bp.route("/areacharts", methods=["GET"])
def area_charts_view():
    return render_template(
        "area_charts_view.html",
        title="Area Charts"
    )


@charts_bp.route("/circularplots", methods=["GET"])
def circular_plots_view():
    return render_template(
        "circular_plots_view.html",
        title="Circular Plots"
    )


@charts_bp.route("/scatterplots", methods=["GET"])
def scatter_plots_view():
    return render_template(
        "scatter_plots_view.html",
        title="Scatter Plots"
    )


@charts_bp.route("/distributioncharts", methods=["GET"])
def distribution_view():
    return render_template(
        "distributions_charts_view.html",
        title="Distribution"
    )


@charts_bp.route("/mapscharts", methods=["GET"])
def maps_view():
    return render_template(
        "maps_charts_view.html",
        title="Maps"
    )


@charts_bp.route("/tablescharts", methods=["GET"])
def tables_view():
    return render_template(
        "tables_charts_view.html",
        title="Tables"
    )

@charts_bp.route("/barchart-of-categories", methods=["GET"])
def bar_of_categories():
    return render_template(
        "barchart_of_categories.html"
    )

@charts_bp.route("/barchart-w-description", methods=["GET"])
def barchart_w_description():
    return render_template(
        "barchart_w_description.html"
    )

@charts_bp.route("/composed-chart", methods=["GET"])
def composed_chart():
    return render_template(
        "layeredchart.html"
    )

@charts_bp.route("/horizontalbarchart", methods=["GET"])
def horizontal_barchart():
    return render_template(
        "stackedbarchart.html"
    )