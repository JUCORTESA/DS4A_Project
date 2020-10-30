import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from scripts.utils import my_dash_components as mydbc
from app import app
from dash.dependencies import Input, Output
from data import run_query, engine
import plotly.express as px


styles = {
    'container': {
        'position': 'fixed',
        'display': 'flex',
        'flex-direction': 'column',
        'height': 'auto',
        'width': '100%'
    }
}

cities = run_query("select DISTINCT(Poblacion) from historicopedidos", engine).poblacion.fillna(0).unique()
#df = get_product_df()

content = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(id="city", options=[{'label': i, 'value': i} for i in cities],
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

    df = run_query("select Material, UM, Poblacion, Fecha_Pedido from  "
                   "historicopedidos WHERE Fecha_Pedido >= "
                   + "\'" + start_date + "\'" + " AND Fecha_Pedido < "
                   + "\'" + end_date + "\'", engine)

    if city:
        df2 = df[df['poblacion'].isin(city)]
    else:
        df2 = df[
            (df['fecha_pedido'] > start_date) & (
                        df['fecha_pedido'] < end_date)]

    fig = px.bar(df2, x='um', y='material', color='um')
    return fig
