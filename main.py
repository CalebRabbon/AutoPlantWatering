import pandas as pd
import pandasql
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import sheets


name = "Live Moisture Data"
sheet = sheets.gSheetsConnect("moistureSensor")
time = sheets.getTime(sheet)
moisturelevel = sheets.getData1(sheet)
# using map() to
# perform conversion from str list to int list
moisturelevel = list(map(int, moisturelevel))

#Step 2: Dash webapp design using CSS and dash app initialization
external_stylesheets = ['cssSheet.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Moisture Sensor Level'

# Graph Colors
darkteal = '#003F5C'
purple = '#58505D'
pink = '#BC5090'
salmon = '#FF6361'
yellow = '#FFA600'

# Areas of the webpage
backgroundcolor = '#00FFFF'
textcolor = '#00FFFF'
black = '#000000'
white = '#FFFFFF'
graphbgcolor = darkteal
aroundgraphcolor = darkteal
xtickcolor = pink
ytickcolor = pink
graphbarcolor = yellow
titlecolor = yellow
xaxiscolor = yellow
yaxiscolor = yellow

figure = go.Figure(data=go.Bar(name="dict", x=time, y=moisturelevel,marker_color=graphbarcolor))
figure.update_yaxes(tick0=0, dtick=5)

figure.update_layout(barmode='group')
figure.layout = {
    'title': dict(
        text=name,
        x = 0.5,
        font=dict(
            family='Courier New, monospace',
            size=24,
            color=titlecolor
        )
    ),
    'xaxis' : dict(
        title='Time',
        titlefont=dict(
            family='Courier New, monospace',
            size=24,
            color=xaxiscolor
        )
    ),
    'yaxis' : dict(
        title='Moisture (%) - Max=47%',
        titlefont=dict(
            family='Courier New, monospace',
            size=24,
            color=yaxiscolor
        )
    )
}
figure.layout.plot_bgcolor = graphbgcolor
figure.layout.paper_bgcolor = aroundgraphcolor
figure.update_xaxes(tickangle=0, tickfont=dict(family='Courier New, monospace', color=xtickcolor, size=14))
figure.update_yaxes(tickangle=0, tickfont=dict(family='Courier New, monospace', color=ytickcolor, size=14))
figure.update_layout(xaxis=dict(showgrid=False, zeroline=False),yaxis=dict(showgrid=False, zeroline=False))
figure.update_traces(marker_line_width=0)
figure.update_layout(
    legend=dict(
        font=dict(
            family='Courier New, monospace',
            size=16,
            color=black,

        ),
        bgcolor=white,
        bordercolor=black,
        borderwidth=2
    )
)
figure.update_layout(hovermode='x')

app.layout = html.Div(children=[

    dcc.Graph(
        id='example-graph',
        figure=figure
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
