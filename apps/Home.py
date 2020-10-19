import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
# local imports
from app import app


HEADER_IMAGE = "/assets/img/medellin.jpg"

layout = html.Div([
    # header image
    html.Img(src=app.get_asset_url(HEADER_IMAGE), style={
        'background-image': 'url("/assets/img/medellin.jpg")',
        'opacity': '0.6',
        '-ms-background-size': 'contain',
        'padding': '100px',
        'background-repeat': 'no-repeat',
        'background-size': 'cover',
        'background-position': 'center',
        'width': '100%',
        'height': 'auto',
        'display': 'block'
    }),
    # title
    dbc.Row([
        dbc.Col(html.H1(
            children="Teaté Colombia S.A.S.",
            className="text-center",
            style={'font-size': '36px', 'color': '4d4d4d',
                   'text-shadow': '2px 8px 6px rgba(0,0,0,0.2), '
                                  '0px -5px 35px rgba(255,255,255,0.3)'})
                , className="mb-5 mt-0 p-0")  # PAGE TITLE
    ], style={'padding': '0', 'margin': '0', 'padding-left': '150px'}),

    # text
    dbc.Row([
        dbc.Col(html.H5(
            children="The neighborhood shops are one of the most important sales "
                     "channels in Colombia for fast-moving consumer goods, representing more than 50% of the total sales. "
                     "Moreover, four out of five Colombian households buy their basic foods from these types of stores due to "
                     "their offer of low prices and convenient products. However, these small businesses are highly inefficient"
                     "these businesses and their suppliers need tools that allow them to achieve greater efficiency in their operations. "
                     "One of such tools is to have an accurate sales forecast that can help both the neighborhood shops and the product manufacturers "
                     "optimize their supply chains and provide the required products at the right moment. This would allow them to achieve greater service "
                     "levels and minimize their losses.",


            style={'font-size': '20px', 'color': '4d4d4d',
                   'text-shadow': '2px 8px 6px rgba(0,0,0,0.2), 0px -5px '
                                  '35px rgba(255,255,255,0.3)'}),
            className="mb-5 mt-0 p-0")
    ], style={'padding': '0', 'margin': '0', 'padding-left': '300px'}),

    # upload bottom
    dbc.Row([dcc.Upload(id='upload-data',
                        children=html.Button('Upload File')),
             ], style={'padding': '0', 'margin': '0', 'padding-left': '150px'},
            className="mb-5", justify="center"),

    # Cards to link to prediction and graphs
    dbc.Row([

        dbc.Col(dbc.Card(children=[
            html.H5(children='Maps interaction with store geolocation',
                    className="text-center"),

            dbc.Button(
                html.Span([html.I(className=""), "Geolocation"]),
                href="",
                target="_blank",
                color="primary",
                className="mt-3"),

            ],
                         body=True, color="dark", outline=True)
                , width=2, className="mb-1"),

        dbc.Col(dbc.Card(children=[

            html.H5(
                children='Analysis of store insights',
                className="text-center"),

            dbc.Button(
               html.Span([html.I(
                   className=""),
                          "Store Analysis"]),
               href="",
               target="_blank",
               color="primary",
               className="mt-3"),

               ],
                         body=True, color="dark", outline=True)
                , width=2, className="mb-2"),

        dbc.Col(dbc.Card(children=[
            html.H5(children='Sales forecst by product',
                    className="text-center"),

            dbc.Button(
                html.Span([html.I(className=""), "Forecast"]),
                href="",
                target="_blank",
                color="primary",
                className="mt-3"),

        ],
            body=True, color="dark", outline=True)
            , width=2, className="mb-3"),

        dbc.Col(dbc.Card(children=[
            html.H5(children='Overall business analysis',
                    className="text-center"),

            dbc.Button(
                html.Span([html.I(className=""), "Data Exploration"]),
                href="",
                target="_blank",
                color="primary",
                className="mt-3"),

        ],
            body=True, color="dark", outline=True)
            , width=2, className="mb-4"),

    ], style={'padding': '0', 'margin': '0', 'padding-left': '150px'},
        className="mb-5", justify="center"),

])
