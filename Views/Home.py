import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from scripts.utils import generate_card


df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

page = dbc.Container(
    [
        html.Div(className = "col-md-8", children = [
            generate_card("Hola", "Cuerpo", dcc.Graph(figure=fig))
        ]),
        html.H1("Iris k-means clustering"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(html.Div(dcc.Graph(figure=fig)), md=6),
                dbc.Col(html.Div(dcc.Graph(
                    id='example-graph',
                figure={
                    'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                            {'x': [1, 2, 3], 'y': [1, 3, 6], 'type': 'bar', 'name': u'Colombia'}
                            ],
                    'layout': {
                        'title': 'Dash Data Visualization PRUEBA'
                    }
        })), md=6),],
            align="center",
        ),
    ],
    fluid=True,
)