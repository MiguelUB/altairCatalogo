import altair as alt
from vega_datasets import data
import random

source = data.cars()
range_ = ['red', 'green', 'blue']

alt.themes.enable("accesible_theme")

for i in range(0, 2):
    pos = random.randint(0, len(source))
    print(pos)
    source.at[pos, 'Origin'] = str(i)

print(source.at[0, 'Origin'])
domain= source['Origin'].tolist()
sche = alt.Diverging("pinkyellowgreen-6")

proba = alt.Chart(source).mark_circle(size=60).encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color=alt.Color('Origin').scale(scheme='blueorange-'),
    tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()

proba.save("hola.html")