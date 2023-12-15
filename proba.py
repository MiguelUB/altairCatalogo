import altair as alt
import numpy as np

import pandas as pd
import altair as alt
from ub_accesible_theme_altair.utils import create_accesible_scheme
from vega_datasets import data

alt.themes.enable('dark_accessible_theme')

source = data.iowa_electricity()

base=alt.Chart(source).mark_area().encode(
    x="year:T",
    y="net_generation:Q",
    color="source:N"
)

base.save('proba.html')

create_accesible_scheme(base, 'proba_accesible')