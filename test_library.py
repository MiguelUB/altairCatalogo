import altair as alt
import pandas as pd
from altair_easeviz import create_accessible_scheme, generate_description
from vega_datasets import data
from altair_easeviz.models import AccessibleTheme

# Instance theme to change grid
acessible_theme = AccessibleTheme()
acessible_theme.change_grid_show()
# Enable Theme
alt.themes.enable('accessible_theme')
# Define chart
source = data.cars()

brush = alt.selection_interval(resolve='global')

base = alt.Chart(source).mark_point().encode(
    y='Miles_per_Gallon',
    color=alt.condition(brush, 'Origin', alt.ColorValue('gray')),
).add_params(
    brush
).properties(
    width=250,
    height=250
)

chart = base.encode(x='Horsepower') | base.encode(x='Acceleration')

# We render the description in an HTML
create_accessible_scheme(chart, 'test')
