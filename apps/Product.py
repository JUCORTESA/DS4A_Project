import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from scripts.utils import my_dash_components as mydbc
from data import get_product_df
import plotly.graph_objects as go
from app import app
from dash.dependencies import Input, Output
import datetime as dt



styles = {
    'container': {
        'position': 'fixed',
        'display': 'flex',
        'flex-direction': 'column',
        'height': 'auto',
        'width': '100%'
    }
}
df = get_product_df()

content = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(id="city", options=[{'label': i, 'value': i} for i in df.Población.unique()],
                                     multi=True, value=['Medellín']))
            ]),
        dbc.Row(
            [
                dcc.DatePickerRange(id="my-date-picker-range",
                                    start_date="2020-01-07",
                                    end_date="2020-05-07",
                                    end_date_placeholder_text='Select a date!'
                                    )
            ]),

        dbc.Row([
            html.Div(children=[dcc.Graph(id='live-graph')]
                     )
        ])
    ]
)

layout = html.Div(children=[
    mydbc.card(content=content, title="Product Analysis",
               description="Here you can find interesting data about Teaté's products",
               color="light", footer="")
], className="my-2")

@app.callback(Output('live-graph', 'figure'),
              [Input('my-date-picker-range', 'start_date'),
               Input('my-date-picker-range', 'end_date'),
               Input('city', 'value')])
def update_graph(start_date, end_date, city):
    start_date = dt.datetime.strptime(start_date, '%Y-%m-%d')

    end_date = dt.datetime.strptime(end_date, '%Y-%m-%d')

    if city:
        df2 = df[
            (df['Fecha Pedido'] > start_date) & (df['Fecha Pedido'] < end_date)
            ]
        df2 = df2[df2['Población'].isin(city)]
    else:
        df2 = df[
            (df['Fecha Pedido'] > start_date) & (df['Fecha Pedido'] < end_date)]

    fig = go.Figure(data=go.Bar(x=df2['UM'], y=df2['Material']))
    return fig

