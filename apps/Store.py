import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from scripts.utils import my_dash_components as mydbc


city_lbl = ["Cali", "Medellín"]
mfr_lbl = ["Colanta", "Alquería", "Leche la Mejor"]
prod_type_lbl = ["Lacteos", "Harinas", "Bebidas Gaseosas"]
prod_lbl = ["Leche Alquería 900 ml", "Leche Alquería 450 ml", "Leche Colanta"]

styles = {
    'container': {
        'position': 'fixed',
        'display': 'flex',
        'flex-direction': 'column',
        'height': 'auto',
        'width': '100%'
    }
}

content = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(mydbc.dropdown(label="City", list_options=city_lbl)),
                dbc.Col(mydbc.dropdown(label="Manufacturer",
                                       list_options=mfr_lbl)),
                dbc.Col(mydbc.dropdown(label="Product type",
                                       list_options=prod_type_lbl)),
                dbc.Col(
                    mydbc.dropdown(label="Product", list_options=prod_lbl)),
            ]),
        dbc.Row(
            children=[
                dbc.Col(dbc.Button("Run Predictor", color="primary",
                                   className="col-8")),
                dbc.Col(children=[
                    html.Div(children=[mydbc.date_picker(label="Date Interval",
                                                         id="date-picker")],
                             className="float-right")
                ], className="col-4 justify-content-start"),

            ]),
        dbc.Row([
            html.Div(className="embed-responsive embed-responsive-16by9",
                     children=[
                         dcc.Graph(id='example-graph',
                                   figure={
                                       'data': [
                                           {'x': ["Tienda Yoli", "Tienda Yary", "Tienda Y Variedades Samuel"], 'y': [3, 4, 4],
                                            'type': 'bar',
                                            'name': 'Product'},
                                       ],
                                       'layout': {
                                           'title': 'Store Visualization',
                                       }
                                   },
                                   className="embed-responsive-item")
                     ],
                     )
        ])
    ]
)

layout = html.Div(children=[
    mydbc.card(content=content, title="Forecast",
               description="Here you can find interesting data about Teaté's products forecast",
               color="light", footer="footer")
], className="my-2")

