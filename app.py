from flask import Flask
import altair as alt
from flask import Flask, render_template
from vega_datasets import data

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here

    cars = data.cars()

    # make the chart
    chart = alt.Chart(cars).mark_point().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
    ).interactive()
    chart.save('chart.html')

    return render_template('./chart.html')


if __name__ == '__main__':
    app.run()
