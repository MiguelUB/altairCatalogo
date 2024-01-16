import os

from flask import Flask
import altair as alt
from flask import Flask, render_template
from vega_datasets import data

from src.api.api import api_bp
from src.views.charts_view import charts_bp

app = Flask(__name__)

app.register_blueprint(charts_bp)
app.register_blueprint(api_bp)
@app.route('/')
def hello_world():  # put application's code here

    return render_template('home.html')


