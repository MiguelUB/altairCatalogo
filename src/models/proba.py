import altair as alt


def y_axis():
    return {'config': {
        'axis': {'domain': True, 'domainColor': '#666F89', 'grid': False, 'gridCap': 'round', 'gridColor': '#B3B7C4',
                 'gridDash': [2, 4], 'gridWidth': 0.5, 'labelColor': '#666F89',
                 'labelFont': 'Roboto, Arial, sans-serif', 'labelPadding': 2, 'tickColor': '#666F89',
                 'tickOpacity': 0.5, 'tickSize': 4, 'titleColor': '#19274E', 'titleFont': 'Roboto, Arial, sans-serif',
                 'titleFontSize': 12}, 'axisBand': {'domain': True, 'labelPadding': 4, 'ticks': False},
        'axisY': {'domain': False, 'titleAlign': 'left', 'titleAngle': 0, 'titleX': -20, 'titleY': -10},
        'legend': {'labelColor': '#666F89', 'labelFont': 'Roboto, Arial, sans-serif', 'labelFontSize': 12,
                   'symbolSize': 40, 'titleColor': '#19274E', 'titleFont': 'Roboto, Arial, sans-serif',
                   'titleFontSize': 12, 'titlePadding': 4}, 'arc': {'stroke': '#FFFFFF', 'strokeWidth': 1},
        'bar': {'fill': '#2770EB', 'stroke': None}, 'line': {'stroke': '#2770EB', 'strokeWidth': 2},
        'path': {'stroke': '#2770EB', 'strokeWidth': 0.5},
        'point': {'fill': '#2770EB', 'shape': 'circle', 'filled': True}, 'rect': {'fill': '#2770EB'},
        'rule': {'stroke': '#666F89'}, 'shape': {'stroke': '#2770EB'},
        'text': {'color': '#19274E', 'font': 'Roboto, Arial, sans-serif', 'fontSize': 12},
        'range': {'category': ['#2770EB', '#77B98A', '#DA5252', '#FFC400', '#A87AEA', '#00A39E', '#19274E'],
                  'diverging': ['#006360', '#2BB3AE', '#96D9D7', '#FFFFFF', '#EDAAAA', '#DA5252', '#811D1D'],
                  'heatmap': ['#18448F', '#1B4EA5', '#2770EB', '#4C88EE', '#82ACF3', '#A6C4F7', '#E9F1FD'],
                  'ramp': ['#18448F', '#1B4EA5', '#2770EB', '#4C88EE', '#82ACF3', '#A6C4F7', '#E9F1FD']},
        'background': '#FFFFFF', 'group': {'fill': '#FFFFFF'},
        'header': {'labelColor': '#19274E', 'labelFont': 'Roboto, Arial, sans-serif', 'labelFontSize': 12,
                   'titleColor': '#19274E', 'titleFont': 'Roboto, Arial, sans-serif', 'titleFontSize': 16},
        'title': {'anchor': 'start', 'color': '#19274E', 'font': 'Roboto, Arial, sans-serif', 'fontSize': 20,
                  'fontWeight': 'bold', 'offset': 20, 'subtitleColor': '#19274E', 'subtitleFontSize': 16},
        'view': {'continuousHeight': 300, 'continuousWidth': 400, 'stroke': 'transparent'}}}


alt.themes.register("y_axis", y_axis)
alt.themes.enable("default")
